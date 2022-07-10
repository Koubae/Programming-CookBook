C ++
=====


* [isocpp.org](https://isocpp.org/get-started)


Installation
------------


```bash
sudo apt-get update

# install c++ 
sudo apt install build-essential gdb g++ 
# install particular version 
sudo apt install build-essential gdb g++-10

# Install multiple g++ compiler versions on Ubuntu 20.04

sudo apt install build-essential
sudo apt -y install g++-7 g++-8 g++-9 g++-10

```

Uninstall
---------



```bash
sudo apt purge --autoremove -y g++

# specific version

sudo apt purge --autoremove -y g++-11


```


Run a Programm
--------------




```bash
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


```


Documentations
--------------


* [Welcome back to C++ - Modern C++](https://docs.microsoft.com/en-us/cpp/cpp/welcome-back-to-cpp-modern-cpp?view=msvc-170)
* [Using the Visual Studio IDE for C++ Desktop Development](https://docs.microsoft.com/en-us/cpp/ide/using-the-visual-studio-ide-for-cpp-desktop-development?view=msvc-170)

### Linux

* [Linux development with C++ | Create and debug applications for Linux](https://docs.microsoft.com/en-us/cpp/linux/?view=msvc-170)
* [Linux development with C++ in Visual Studio](https://devblogs.microsoft.com/cppblog/linux-development-with-c-in-visual-studio/)

### g++ 

* [g++ - is using the "-g" flag for production builds a good idea?](https://stackoverflow.com/questions/10988318/g-is-using-the-g-flag-for-production-builds-a-good-idea)
* [How Does The Debugging Option -g Change the Binary Executable?](https://stackoverflow.com/questions/89603/how-does-the-debugging-option-g-change-the-binary-executable)
* []()

```
-g tells the compiler to store symbol table information in the executable. Among other things, this includes:
```


Repos
--------------

* [christopher-siewert/cpp-calculator(https://github.com/christopher-siewert/cpp-calculator)
* [microsoft/calculator](https://github.com/microsoft/calculator)