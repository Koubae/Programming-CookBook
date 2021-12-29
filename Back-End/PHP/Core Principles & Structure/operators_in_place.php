<?php
// Inline String Concatenation
$full_name = "Fede";
$full_name .= " Bau";
echo $full_name;


//  With assignment by reference, changes made to one variable will affect the other
$first_player_rank = "Beginner";
$second_player_rank =& $first_player_rank;
echo $second_player_rank; // Prints: Beginner

$first_player_rank = "Intermediate"; // Reassign the value of $first_player_rank
echo $second_player_rank; // Prints: Intermediate
