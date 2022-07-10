
##########################################
#            RUN / BUILD                 #
##########################################

# Build
g++ -o hello_world hello_world.cpp

# Run
./hello_world

# With visual studio code just press f5

# Build with more flags

g++ -fdiagnostics-color=always -g  -o main.o -c main.cpp -std=c++20
# with different compilar
/usr/bin/g++-10 -fdiagnostics-color=always -g  -o main.o -c main.cpp -std=c++20


# Build all file of project (example of calculator_o)
# Credit -> https://askubuntu.com/a/1348231/1166575
# Build main
/usr/bin/g++-10 -fdiagnostics-color=always -g  -o main.o -c main.cpp -std=c++20
# BUild Calculator .cpp
/usr/bin/g++-10 -fdiagnostics-color=always -g  -o Calculator.o -c Calculator.cpp -std=c++20
# Build Final App
/usr/bin/g++-10 -fdiagnostics-color=always  main.o Calculator.o -o calculator
# Run 
./calculator

# Now all of this in one go
/usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Calculator.cpp -o calculator

# Build and run 
/usr/bin/g++-10 -fdiagnostics-color=always -g -std=c++20 main.cpp Calculator.cpp -o calculator && ./calculator
```


Compile `c++` with different versions

```bash 

# with g++ 9 (for c++20 versions)
-std=c++2a
-std=c++17

#-------------------
# pch.h
# Precompiled header --> https://en.wikipedia.org/wiki/Precompiled_header
# ------------------
# https://stackoverflow.com/questions/54121917/what-is-pch-h-and-why-is-it-needed-to-be-included-as-the-first-header-file

# Creadit -> https://stackoverflow.com/questions/70142090/how-to-know-if-compiler-is-taking-advantage-of-the-pch-h-gch-file
g++ -std=c++20 -Wall -O3 -flto pch.h -o pch.h.gch