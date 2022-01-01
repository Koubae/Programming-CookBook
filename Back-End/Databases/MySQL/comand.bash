# Start mysql CLI
mysql -u root 

# Create database
create database [Database]

# Create User
mysql -u adminusername -p
# Enter password:
# Welcome to the MySQL monitor. Commands end with ; or \g.
# Your MySQL connection id is 5340 to server version: 3.23.54

# Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

CREATE DATABASE databasename;
# Query OK, 1 row affected (0.00 sec)

GRANT ALL PRIVILEGES ON databasename.* TO "wordpressusername"@"hostname"
# -> IDENTIFIED BY "password";
# Query OK, 0 rows affected (0.00 sec)

FLUSH PRIVILEGES;
# Query OK, 0 rows affected (0.01 sec) 

EXIT
# Bye
# $ 