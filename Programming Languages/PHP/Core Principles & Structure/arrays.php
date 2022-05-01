<?php

$odd_numbers = [1,3,5,7,9];

// count function returns the number of members an array has.
echo count($odd_numbers), "\n";

//  reset function gets the first member of the array. (It also resets the internal iteration pointer).
$first_item = reset($odd_numbers);

// end function gets the last member of the array.
$last_item = end($odd_numbers);

// To push a member to the end of an array
$numbers = [1,2,3];
array_push($numbers, 4); // now array is [1,2,3,4];
// print the new array
print_r($numbers);
// The same can be achieved in this form
$numbers[] = 5; // now array is [1,2,3,4];
print_r($numbers);


// To pop a member from the end of an array
$numbers = [1,2,3,4];
array_pop($numbers); // now array is [1,2,3];

// print the new array
print_r($numbers);


// To push a member to the beginning of an array
$numbers = [1,2,3];
array_unshift($numbers, 0); // now array is [0,1,2,3];
// print the new array
print_r($numbers);

// To pop a member from the beginning of an array
$numbers = [0,1,2,3];
array_shift($numbers); // now array is [1,2,3];

// print the new array
print_r($numbers);

//  concatenate between two arrays:
$odd_numbers = [1,3,5,7,9];
$even_numbers = [2,4,6,8,10];
$all_numbers = array_merge($odd_numbers, $even_numbers);
print_r($all_numbers);

// Sort an array
$numbers = [4,2,3,1,5];
sort($numbers);
print_r($numbers);

// Slice an Array
$numbers = [1,2,3,4,5,6];
print_r(array_slice($numbers, 3));
print_r(array_slice($numbers, 3, 2)); // offset, length

// array_splice it will also remove the slice returned from the original array
$numbers = [1,2,3,4,5,6];
print_r(array_splice($numbers, 3, 2));
print_r($numbers);


// ---------------------- < Joining and splitting > ---------------------- \\
$fruits = "apple,banana,orange";
$fruit_list = explode(",", $fruits);
print_r($fruit_list);
$fruit_string = implode("--", $fruit_list);
print_r($fruit_string);
