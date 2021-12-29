<?php

// see if key in array
$associative_array = [
    "key_1" => "some_value",
    "key_2" => "some_other_value"
];
if (array_key_exists("key_1", $associative_array)) {
    $value = $associative_array["key_1"];
    echo "key_1 in array $value\n";
}
if (!array_key_exists("nope", $associative_array)) {
    echo 'Value dont exists' . "\n";
}

// Get only keys
print_r(array_keys($associative_array));
// Get only Values
print_r(array_values($associative_array));
