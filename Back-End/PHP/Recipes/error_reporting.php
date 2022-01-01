<?php 
// this in your index.php file:
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

// this doesn't make PHP to show parse errors - the only way to show those errors is to modify your php.in
// display_errors = on
// if you don't have access to php.ini, then putting this line in .htaccess might work too

// php_flag display_errors 1

?>

<?php // if you only want to see Errors and Warnings - but not Notices - then you can configure that:
error_reporting(E_ERROR | E_WARNING);

?>

<?php // Inline Error Suppression
echo @$foo['bar'];

?>
<!-- Xdebug has an xdebug.scream in the ini setting-->
xdebug.scream = On

<!-- Or in run time -->
<?php ini_set('xdebug.scream', '1') ?>

