-- Credit https://stackoverflow.com/a/28890883/13903942
CREATE TABLE accounts(
    account_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT( 4 ) NOT NULL ,
    account_type ENUM( 'savings', 'credit' ) NOT NULL,
    balance FLOAT( 9 ) NOT NULL,
    PRIMARY KEY ( account_id )
)

and

CREATE TABLE customers(
    customer_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
)

-- How do I create a 'relationship' between the two tables? I want each account to be 'assigned' one customer_id (to indicate who owns it).
--If you want to have a strict 1 to 1 relationship, just merge the two tables.
CREATE TABLE customers(
    customer_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
    account_type ENUM( 'savings', 'credit' ) NOT NULL,
    balance FLOAT( 9 ) NOT NULL,
)


-- create a relationship table.
CREATE TABLE customersaccounts(
    customer_id INT NOT NULL,
    account_id INT NOT NULL,
    PRIMARY KEY (customer_id, account_id),
    FOREIGN KEY customer_id references customers (customer_id) on delete cascade,
    FOREIGN KEY account_id  references accounts  (account_id) on delete cascade
}

-- if you have a customer_id and want the account info, you join on customersaccounts and accounts:
SELECT a.*
    FROM customersaccounts ca
        INNER JOIN accounts a ca.account_id=a.account_id
            AND ca.customer_id=mycustomerid;

--Also create a VIEW
CREATE VIEW customeraccounts AS 
    SELECT a.*, c.* FROM customersaccounts ca
        INNER JOIN accounts a ON ca.account_id=a.account_id
        INNER JOIN customers c ON ca.customer_id=c.customer_id;