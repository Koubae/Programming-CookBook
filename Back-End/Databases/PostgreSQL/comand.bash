# ========================= < Command Lines > ========================= #



# --------------- >  Admin

# PostgreSQL interactive terminal
# DOCS => https://www.postgresql.org/docs/13/app-psql.html

psql -U [user_name] -d [db_name]

EXIT

# current version of PostgreSQL

SELECT version();

# list the tables in the current database

\dt   

# PERFORM a SQL query insted

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;



# --------------- >User



# --------------- > Database


CREATE DATABASE [Database_name]

CREATE DATABASE [db_name] OWNER [owner_name] 

#To switch databases PSQL:

\connect database_name 
\c database_name

# List all DBs

\list 
\l

SELECT datname FROM pg_database
WHERE datistemplate = false;


#


# --------------- > Table

# List All tables in current DB
\dt

# List all tables in current DB regardless of your search_path
\dt *

# pg_restore tool to load data into the dvdrental database

pg_restore -U [username] -d [db_name] [File_path]

# restore PostgreSQL database from .tar file?

# https://www.postgresql.org/docs/7.3/app-pgrestore.html

pg_restore -W -c -i -U postgres -d client03 -v "/tmp/client03.tar";

-c     # to clean the database
-i     # to ignore any database version checks
-U     # to force a user
-d     # to select the database
-v     # verbose mode, don't know why
"$$"   # the location of the files to import in tmp to get around permission issues
-W     # to force asking for the password to the user (postgres)

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