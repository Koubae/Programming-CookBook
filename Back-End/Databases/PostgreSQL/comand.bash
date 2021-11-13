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

# Drop table

DROP TABLE IF EXISTS  [name]  CASCADE;