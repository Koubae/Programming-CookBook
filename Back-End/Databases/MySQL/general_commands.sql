-- login

mysql -u adminusername -p


-- create database
> CREATE DATABASE database_name COLLATE utf8mb4_general_ci;

-- create user

CREATE USER "admin" IDENTIFIED BY "pass";
GRANT ALL PRIVILEGES ON database_name.* TO "admin";

