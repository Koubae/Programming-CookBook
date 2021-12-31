/*Some usefull reference
Should we ever check for mysqli_connect() errors manually? --> https://stackoverflow.com/a/58808333/13903942
Should I manually check for errors when calling "mysqli_stmt_prepare"? --> https://stackoverflow.com/questions/62216426/should-i-manually-check-for-errors-when-calling-mysqli-stmt-prepare
https://phpdelusions.net/mysqli
https://phpdelusions.net/mysqli/mysqli_connect#error_handling
https://www.php.net/manual/en/mysqli.construct.php
*/

<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

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

?>
// Variant 

<?php
$host = '127.0.0.1';
$port = 3306;
$db   = 'test';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';
?>

<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
try {
    require __DIR__.'/db_credentials.php';
    $db = new mysqli($host, $user, $pass, $db, $port);
    $db->set_charset($charset);
    $db->options(MYSQLI_OPT_INT_AND_FLOAT_NATIVE, 1);
} catch (\mysqli_sql_exception $e) {
     throw new \mysqli_sql_exception($e->getMessage(), $e->getCode());
} finally {
    unset($host, $db, $user, $pass, $charset);
}

function prepared_query($db, $sql, $params, $types = "")
{
    $types = $types ?: str_repeat("s", count($params));
    $stmt = $db->prepare($sql);
    $stmt->bind_param($types, ...$params);
    $stmt->execute();
    return $stmt;
}
?>
