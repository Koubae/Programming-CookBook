<?php 
// Example with MySQL and SQLite
// PDO + MySQL
$pdo = new PDO('mysql:host=example.com;dbname=database', 'user', 'password');
$statement = $pdo->query("SELECT some_field FROM some_table");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['some_field']);

// PDO + SQLite
$pdo = new PDO('sqlite:/path/db/foo.sqlite');
$statement = $pdo->query("SELECT some_field FROM some_table");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['some_field']);
?>

<?php 
// Safe query against SQL Against
$pdo = new PDO('sqlite:/path/db/users.db');
$stmt = $pdo->prepare('SELECT name FROM users WHERE id = :id');
$id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT); // <-- filter your data first (see [Data Filtering](#data_filtering)), especially important for INSERT, UPDATE, etc.
$stmt->bindParam(':id', $id, PDO::PARAM_INT); // <-- Automatically sanitized for SQL by PDO
$stmt->execute();

?>


<?php
// Create a new connection.
// You'll probably want to replace hostname with localhost in the first parameter.
// Note how we declare the charset to be utf8mb4.  This alerts the connection that we'll be passing UTF-8 data.  This may not be required depending on your configuration, but it'll save you headaches down the road if you're trying to store Unicode strings in your database.  See "Gotchas".
// The PDO options we pass do the following:
// PDO::ATTR_ERRMODE enables exceptions for errors.  This is optional but can be handy.
// PDO::ATTR_PERSISTENT disables persistent connections, which can cause concurrency issues in certain cases.  See "Gotchas".
$link = new PDO(    'mysql:host=your-hostname;dbname=your-db;charset=utf8mb4',
                    'your-username',
                    'your-password',
                    array(
                        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                        PDO::ATTR_PERSISTENT => false
                    )
                );
 
$handle = $link->prepare('select Username from Users where UserId = ? or Username = ? limit ?');
 
$handle->bindValue(1, 100);
$handle->bindValue(2, 'Bilbo Baggins');
$handle->bindValue(3, 5);
 
$handle->execute();
 
// Using the fetchAll() method might be too resource-heavy if you're selecting a truly massive amount of rows.
// If that's the case, you can use the fetch() method and loop through each result row one by one.
// You can also return arrays and other things instead of objects.  See the PDO documentation for details.
$result = $handle->fetchAll(PDO::FETCH_OBJ);
 
foreach($result as $row){
    print($row->Username);
}
?>