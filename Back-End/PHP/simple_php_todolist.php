/**
Credits  codecademy.com 
This script is made by codecademy (free version) of the PHP course 
https://www.codecademy.com/courses/learn-php/lessons/intro-php/exercises/todo-learn-php

*/

<?php
require 'vendor/autoload.php';
# This logic handles connecting to the database, where we store our todo status
$pdo = new \PDO("sqlite:" . "db/sqlite.db");

# This PHP logic handles user actions
# New TODO
if (isset($_POST['submit'])) 
{
  $description = $_POST['description'];
  $sth = $pdo->prepare("INSERT INTO todos (description) VALUES (:description)");
  $sth->bindValue(':description', $description, PDO::PARAM_STR);
  $sth->execute();
}
# Delete TODO
elseif (isset($_POST['delete']))
{ 
  $id = $_POST['id'];
  $sth = $pdo->prepare("delete from todos where id = :id");
  $sth->bindValue(':id', $id, PDO::PARAM_INT);
  $sth->execute();
}
# Update completion status
elseif (isset($_POST['complete']))
{
    $id = $_POST['id'];
    $sth = $pdo->prepare("UPDATE todos SET complete = 1 where id = :id");
    $sth->bindValue(':id', $id, PDO::PARAM_INT);
    $sth->execute();
}
# Here is the HTML:
?>
<!DOCTYPE HTML>
<html lang="en">
<head>
  <title>Todo List</title>
</head>

<body class="container">
  <h1>Todo List</h1>
  <form method="post" action="">
    <input type="text" name="description" value="">
    <input type="submit" name="submit" value="Add">
  </form>
  <h2>Current Todos</h2>
  <table class="table table-striped">
    <thead><th>Task</th><th></th><th></th></thead>
    <tbody>

<?php
  # Entering PHP mode, 
$sth = $pdo->prepare("SELECT * FROM todos ORDER BY id DESC");
$sth->execute();

foreach ($sth as $row) {
  # Exiting PHP Mode
    ?> 
<tr>
  <td>
      <!-- This is PHP shorthand for inserting dynamic text into HTML -->
      <?=htmlspecialchars($row['description'])?></td>
  <td>
    <?php # Here we are mixing HTML and PHP to get the desired document
if (!$row['complete']) {
        ?>
    <form method="POST">
      <button type="submit" name="complete">Complete</button>
      <input type="hidden" name="id" value="<?=$row['id']?>">
      <input type="hidden" name="complete" value="true">
    </form>
    <?php
} else {
        ?>
    Task Complete!
    <?php
}
    ?>
  </td>
  <td>
    <form method="POST">
      <button type="submit" name="delete">Delete</button>
      <input type="hidden" name="id" value="<?=$row['id']?>">
      <input type="hidden" name="delete" value="true">
    </form>
  </td>
</tr>
<?php
}
?>
    </tbody>
  </table>
</body>
</html>