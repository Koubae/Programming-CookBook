C ++
=====


* [isocpp.org](https://isocpp.org/get-started)
* [A Tour of C++](https://isocpp.org/tour)
* [C++ Team Blog](https://devblogs.microsoft.com/cppblog/)

* [https://github.com/salmer/CppDeveloperRoadmap](https://github.com/salmer/CppDeveloperRoadmap)

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
* [C++ Language Reference](https://assets.ctfassets.net/9pcn2syx7zns/41G6GBcYuIvsds5OG3H2OQ/f222a11333041e193e9de8b393b71653/language_refreence.pdf)
* [C++ Quick Language Reference](http://kali.azc.uam.mx/clc/03_docencia/licenciatura/i_programacion/Libro_C++.pdf)
* [C++ Standard Library Containers](https://docs.microsoft.com/en-us/cpp/standard-library/stl-containers?view=msvc-170)

* [Documenting C++](https://developer.lsst.io/cpp/api-docs.html)
 

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

Projects
--------

* [CMake](https://cmake.org/)
* [CMake projects in Visual Studio](https://docs.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170)

Repos
--------------

* [christopher-siewert/cpp-calculator(https://github.com/christopher-siewert/cpp-calculator)
* [microsoft/calculator](https://github.com/microsoft/calculator)



Tutorials
---------

### Microsoft 

* [Get started with C++ and C](https://docs.microsoft.com/en-us/cpp/?view=msvc-170)
* [C++ language documentation](https://docs.microsoft.com/en-us/cpp/cpp/?view=msvc-170)
* [C++ Language Reference](https://docs.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170)
* [C++ Standard Library Overview](https://docs.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-overview?view=msvc-170)
* [Linux development with C++ | Create and debug applications for Linux](https://docs.microsoft.com/en-us/cpp/linux/?view=msvc-170)
* [Linux development with C++ in Visual Studio](Linux development with C++ in Visual Studio)

### Cool 

* [isocpp.org](https://isocpp.org/get-started)
* []()
* []()

### Misc

* [Best C++ Documentation](https://obiztools.com/best-c-documentation/)

Terms & Keywords
-----------------

### Basic structs

* array
* map
* vector
* set
* multimap
* multiset
* unordered_multimap
* unordered_multiset
* [C++ Standard Library Containers](https://docs.microsoft.com/en-us/cpp/standard-library/stl-containers?view=msvc-170)
* deque
* list
* forward_list 

* queue
* priority_queue
* stack 

* [Range-based for Statement (C++)](https://docs.microsoft.com/en-us/cpp/cpp/range-based-for-statement-cpp?view=msvc-170)

### Mist



* *resource acquisition is initialization **(RAII)***