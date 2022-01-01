// Credit --> https://phpbestpractices.org
<?php
// Hash the password.  $hashedPassword will be a 60-character string.
$hashedPassword = password_hash('my super cool password', PASSWORD_DEFAULT);
 
// You can now safely store the contents of $hashedPassword in your database!
 
// Check if a user has provided the correct password by comparing what they typed with our hash
password_verify('the wrong password', $hashedPassword); // false
 
password_verify('my super cool password', $hashedPassword); // true
?>