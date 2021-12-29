<?php

$DB_HOST = "localhost";
$DB_USER_NAME = "root";
$DB_PASSWORD = "";
$DB_NAME = "MyDatabase";
$DB_TABLE_FILE = "db_tables.sql";
// Create connection
$conn = new mysqli($DB_HOST, $DB_USER_NAME, $DB_PASSWORD);
// Check connection
if ($conn->connect_errno) {
	echo "MySQL connection failed.<br>";
	die("Connection failed: " . $conn->connect_error);
} else {

}

// DB create
if($conn->query('CREATE DATABASE IF NOT EXISTS '.$DB_NAME.';') === TRUE){

}else {
	echo  "Error: ".$conn->errno.", ".$conn->error."<br>";
}

// DB Creates Tables
$DB_TABLES = file_get_contents("./" . $DB_TABLE_FILE);
if($conn->multi_query($DB_TABLES) !== TRUE){
	echo "Error: ".$conn->errno.", ".$conn->error."<br>";
} else {
	// Need to consume the SQL execution
	while ($conn->next_result());
	// Connected successfully
}
