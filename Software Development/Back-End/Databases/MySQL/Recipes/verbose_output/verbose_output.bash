# Credit --> https://dba.stackexchange.com/a/14307/222739
# If you are trying to catch any output based on errors, try this:
# Using 2> will catch any error-based output (aka stderr). The mysqldump should still pipe normal 
# console output (aka stdout) to the other mysql session and load the data as intended.
mysqldump -alv -h 123.123.123.123 --user=username --password=p@ssw0rd --add-drop-table databasename 2> output.log | mysql --user=username --password=p@ssw0rd -h localhost localdatabase


# ----------------

mysqldump -u... -p... --verbose sample 2>sample.txt > sample.sql

type sample.txt
# -- Connecting to localhost...
# -- Retrieving table structure for table users...
# -- Sending SELECT query...
# -- Retrieving rows...
# -- Disconnecting from localhost...

type sample.sql

# -- MySQL dump 10.13  Distrib 5.5.12, for Win64 (x86)
# --
# -- Host: localhost    Database: sample
# -- ------------------------------------------------------
# -- Server version       5.5.12-log

# /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
# /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
# .....