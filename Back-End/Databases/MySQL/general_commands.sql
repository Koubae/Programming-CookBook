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