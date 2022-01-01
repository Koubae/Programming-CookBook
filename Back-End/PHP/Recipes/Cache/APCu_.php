// https://phpbestpractices.org
<?php
// Store some values in the APCu cache.  We can optionally pass a time-to-live, but in this example the values will live forever until they're garbage-collected by APCu.
apcu_store('username-1532', 'Frodo Baggins');
apcu_store('username-958', 'Aragorn');
apcu_store('username-6389', 'Gandalf');
 
// You can store arrays and objects too.
apcu_store('creatures', array('ent', 'dwarf', 'elf'));
apcu_store('saruman', new Wizard());
 
// After storing these values, any PHP script can access them, no matter when it's run!
$value = apcu_fetch('username-958', $success);
if($success === true){
    print($value); // Aragorn
}
 
$value = apcu_fetch('creatures', $success);
if($success === true){
    print_r($value);
}
 
$value = apcu_fetch('username-1', $success); // $success will be set to boolean false, because this key doesn't exist.
if($success !== true){ // Note the !==, this checks for true boolean false, not "falsey" values like 0 or empty string.
    print('Key not found');
}
 
apcu_delete('username-958'); // This key will no longer be available.