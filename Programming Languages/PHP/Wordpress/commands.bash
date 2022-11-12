# sql commands
#-- create a user
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'wordpress';
#-- list users
SELECT user FROM mysql.user;
#-- create database 
CREATE DATABASE wp_first_app;
#-- Grant access to user
GRANT ALL ON wp_first_app.* TO 'wordpress'@'localhost';
#-- reload privileges
FLUSH PRIVILEGES;
