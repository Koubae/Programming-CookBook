-- sqlite

-- Syntax
column_name data_type 
    [GENERATED ALWAYS] AS expression 
    [VIRTUAL | STORED]

-- GENERATED ALWAYS keywords are optional.
column_name data_type AS expression [VIRTUAL | STORED]


/* ============================ < Example 1 > ============================ */

CREATE TABLE products(
    name TEXT NOT NULL,
    price REAL NOT NULL,
    discount REAL NOT NULL,
    tax REAL NOT NULL,
    net_price REAL GENERATED ALWAYS  -- VIRTUAL 
        AS (price * (1-discount) * (1+tax))
);

-- NOT supply values to the net_price
INSERT INTO products(name, price, discount, tax)
VALUES('ABC Widget',100, 0.05, 0.07);



-- FAQ:
If a generated column is VIRTUAL, SQLite doesn’t store the values of the column physically. Instead, when you read values from the generated column, SQLite computes these values based on the expression specified in the column declaration.

SQLite uses the VIRTUAL by default when you don’t explicitly specify VIRTUAL or STORED in the generated column declaration.

In case a generated column is STORED, SQLite stores the values of the column physically. In other words, the STORED generated column takes up spaces in the database file. SQLite updates the values of the STORED generated column when you write to the database.


In practice, you use the STORED option when you want to optimize for reading and the VIRTUAL option when you want to optimize for writing.