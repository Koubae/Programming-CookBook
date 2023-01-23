#!/usr/bin/env bash
# @credit: https://stackoverflow.com/a/53063656/13903942

# Compile and run C multiple C Versions of C
for std in c90 c99 c11 c17 c23 gnu89 gnu99 gnu11 gnu17; do
  echo $std
  gcc main.c -std=$std -o c.out
  ./c.out
  echo
done

# This, is the default C that your GCC Compiler will compile (withou -std=[VERSION])
echo default
gcc main.c -o c.out
./c.out