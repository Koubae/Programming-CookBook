<?php
// First, define your auto-load function.
function MyAutoload($className){
    include_once($className . '.php');
}
 
// Next, register it with PHP.
spl_autoload_register('MyAutoload');
 
// Try it out!
// Since we haven't included a file defining the MyClass object, our auto-loader will kick in and include MyClass.php.
// For this example, assume the MyClass class is defined in the MyClass.php file.
$var = new MyClass();
?>