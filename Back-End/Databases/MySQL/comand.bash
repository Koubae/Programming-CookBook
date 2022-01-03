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

GRANT ALL PRIVILEGES ON databasename.* TO "wordpressusername"@"hostname"

FLUSH PRIVILEGES;

EXIT
# Bye
# $ 
# Character Set and Collation
CREATE DATABASE my_first_db DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

