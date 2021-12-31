// this in your index.php file:
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

// this doesn't make PHP to show parse errors - the only way to show those errors is to modify your php.in
display_errors = on
<!-- (if you don't have access to php.ini, then putting this line in .htaccess might work too): -->

php_flag display_errors 1