#!/bin/bash

# Simple C Compile short cut and run script 


DIR=$1;
COMPILE_ONLY=$2;

cd "$DIR";
gcc main.c -o main 

if [[ "$COMPILE_ONLY" == "true" ]]

    then 
        echo "Compiled main in $(pwd). Run with $(pwd)/main" && exit;
    else
        ./main "${@:2}"
fi 