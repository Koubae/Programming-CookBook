-- login

mysql -u adminusername -p


-- create database
> CREATE DATABASE database_name COLLATE utf8mb4_general_ci;

-- create user

CREATE USER "admin" IDENTIFIED BY "pass";
GRANT ALL PRIVILEGES ON database_name.* TO "admin";

-- flush
FLUSH PRIVILEGES;


-- Change Database type 
-- Credit --> https://www.php.net/manual/en/pdo.rollback.php#100847
-- Should anyone reading this be slightly panicked because they just 
--discovered that their MySQL  tables are MyIsam and not InnoDb, 
--don't worry... You can very easily change the storage engine using the following query:

ALTER TABLE your_table_name ENGINE = innodb;


--- Drop ALl Tables 
-- CRedit -> https://stackoverflow.com/a/3476803/13903942

SET FOREIGN_KEY_CHECKS = 0;
drop table if exists customers;
drop table if exists orders;
drop table if exists order_details;
SET FOREIGN_KEY_CHECKS = 1;

-- Also note the following :

-- If you use MySQL Workbench, you can avoid having to type all the table names by
-- selecting all tables in the left column, right-clicking, then 'drop tables' option.

-- IT will generate the SQL which you can copy and paste between the SET FOREGIN_KEY_CHECKS 
-- statement's - probably similar in other GUI's as well. 