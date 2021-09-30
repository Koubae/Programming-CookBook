#  lists tables in the current database

SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,[table_name];


# ---------------> DATABASE SIZE

SELECT pg_database_size('databaseName');


# Pretty formated https://www.postgresonline.com/journal/archives/233-How-big-is-my-database-and-my-other-stuff.html
SELECT pg_size_pretty( pg_database_size( current_database() ) ) As human_size
, pg_database_size( current_database() ) As raw_size;


# ---------------> Combine JOINS + COUNT

SELECT table_a.id, COUNT(t_b.id) 
FROM table_a as t_a
LEFT JOIN table_b as t_b ON
    t_b.rel = t_a.id
GROUP BY t_a.id
ORDER BY COUNT(t_b.id) DESC;

# ---------------> Combine JOINS + COUNT + HAVING


SELECT partner.id, COUNT(res.id) as ResCount
FROM res_partner as partner
LEFT JOIN guest_experience as res ON
    res.partner_id = partner.id
GROUP BY partner.id
HAVING
	COUNT (res.id) >= 2
ORDER BY COUNT(res.id);


# ---------------> Unify Array subquery to JSON


SELECT (SELECT jsonb_agg(re.reservations))
FROM
    (
        SELECT unnest(array_agg(res.id)) as reservations
        FROM res_partner as partner
        LEFT JOIN guest_experience as res ON
            res.partner_id = partner.id
        GROUP BY partner.id
        HAVING
            COUNT (res.id) >= 2

    ) re
;


# ---------------> Count all array subquery

SELECT (SELECT COUNT(re.res_count))
FROM
    (
        SELECT array_agg(res.id) as reservations, COUNT(res.id) as res_count
        FROM res_partner as partner
        LEFT JOIN guest_experience as res ON
            res.partner_id = partner.id
        GROUP BY partner.id
        HAVING
            COUNT (res.id) >= 2

    ) re
;


# ---------------> ARRAY_AGG Unify 2 columns of the same Table

SELEFT ARRAY_AGG(id), res_id  FROM ir_property
WHERE name = 'standard_price'
GROUP BY res_id
HAVING COUNT(res_id) > 1;

# ---------------> ARRAY_AGG leave out Null values in ARRAY_AGG
SELECT ARRAY_AGG(prop.id), prop.res_id , ARRAY_AGG(DISTINCT product.id)
FROM ir_property AS prop
LEFT JOIN product_product AS product ON
    split_part(prop.res_id, ',', 2) = product.id::varchar(255)
WHERE name = 'standard_price'
GROUP BY res_id
HAVING COUNT(res_id) > 1 AND  TRUE = ANY (SELECT unnest(ARRAY_AGG(product.id)) IS NOT NULL);

# ---------------> ARRAY_AGG ANY Null values in ARRAY_AGG

SELECT ARRAY_AGG(prop.id), prop.res_id , ARRAY_AGG(DISTINCT product.id)
FROM ir_property AS prop
LEFT JOIN product_product AS product ON
    split_part(prop.res_id, ',', 2) = product.id::varchar(255)
WHERE name = 'standard_price'
GROUP BY res_id
HAVING COUNT(res_id) > 1 AND  TRUE = ANY (SELECT unnest(ARRAY_AGG(product.id)) IS  NULL);


SELECT  ARRAY_AGG(prop.id), prop.res_id ,  ARRAY_AGG(DISTINCT product.id)
FROM ir_property AS prop
LEFT JOIN product_product AS product ON
    split_part(prop.res_id, ',', 2) = product.id::varchar(255)
WHERE name = 'standard_price'
GROUP BY res_id
HAVING COUNT(res_id) > 1 AND  TRUE <> ALL (SELECT unnest(ARRAY_AGG(product.id)) IS NULL); # Variation, using <> ALL is like NOT 


# ----- DELETING

DELETE FROM ir_property WHERE id IN (
    SELECT  unnest(ARRAY_AGG(prop.id ORDER by prop.id)) AS property_array
    FROM ir_property AS prop
    LEFT JOIN product_product AS product ON
        split_part(prop.res_id, ',', 2) = product.id::varchar(255)
    WHERE name = 'standard_price'
    GROUP BY res_id
    HAVING TRUE = ANY (SELECT unnest(ARRAY_AGG(product.id)) IS NULL)
)



# ----- Index size of all Tables in DB


# https://stackoverflow.com/a/67727882/13903942
SELECT
    relname  as table_name,
    pg_size_pretty(pg_total_relation_size(relid)) As "Total Size",
    pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as "Index Size",
    pg_size_pretty(pg_relation_size(relid)) as "Actual Size"
    FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

# -------- Show all constraints of a given Table

SELECT *
FROM information_schema.constraint_table_usage
WHERE table_name = 'your_table'

# Using  pg_constraint
SELECT n.nspname AS schema_name,
    t.relname AS table_name,
    c.conname AS constraint_name
FRPM pg_constraint c
    JOIN pg_class t ON c.conrelid = t.oid
    JOIN pg_namespace n ON t.relnamespace = n.oid
WHERE t.relname = 'your_table_name';


# ------- ALTER Consraints Drop constraint
ALTER TABLE your_table DROP CONSTRAINT constraint_name;

# ---- Complete Alter Statements
SELECT 'ALTER TABLE '||table_name||' DROP CONSTRAINT '||constraint_name||';'
FROM information_schema.constraint_table_usage
WHERE table_name in ('your_table', 'other_table')