C ++
=====


* [isocpp.org](https://isocpp.org/get-started)
* [A Tour of C++](https://isocpp.org/tour)
* [C++ Team Blog](https://devblogs.microsoft.com/cppblog/)
* [Current Status / C++ Version](https://isocpp.org/std/status)

* [https://github.com/salmer/CppDeveloperRoadmap](https://github.com/salmer/CppDeveloperRoadmap)

#### Relative Projects

* [Koubae/C-CPP-Examples](https://github.com/Koubae/C-CPP-Examples)
* [Koubae/C-Calculator-Simple](https://github.com/Koubae/C-Calculator-Simple)

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

StackOverflow | Forums | QA
-------------


* [What is the weird colon-member (“ : “) syntax in constructor?](https://saikamesh.medium.com/what-is-the-weird-colon-member-syntax-in-constructor-2fd065278d6f)
* [C++, What does the colon after a constructor mean? [duplicate]](https://stackoverflow.com/questions/2785612/c-what-does-the-colon-after-a-constructor-mean)
* [Variables after the colon in a constructor [duplicate]](https://stackoverflow.com/questions/2349978/variables-after-the-colon-in-a-constructor)
* [What does a colon following a C++ constructor name do? [duplicate]](https://stackoverflow.com/questions/1272680/what-does-a-colon-following-a-c-constructor-name-do)


### CLion

* [Multiple Main Source files in CLion](https://intellij-support.jetbrains.com/hc/en-us/community/posts/205823219-Multiple-Main-Source-files-in-CLion)
* [Run/debug single file](https://www.jetbrains.com/help/clion/run-single-file.html?_gl=1*reacd7*_gcl_aw*R0NMLjE3Mjc1NDQwODcuQ2p3S0NBancwdDYzQmhBVUVpd0E1eFA1NFI5OUFYWktvc2JlbWZlWHFDajRhNTZUVTk0ZHowUFNZM01HYjdlNm44YjhOUk1RMEpyQlRob0NZem9RQXZEX0J3RQ..*_gcl_au*MTE1ODc1NDYyMy4xNzI3MTY5ODYw*_ga*MjA1NjYzNjkwNC4xNzI3MTY5ODU5*_ga_9J976DJZ68*MTcyNzYwNTc2OS4zLjEuMTcyNzYwNTkwMS40Ni4wLjA.)
* [developerinsider/C-Programming-Example](https://github.com/developerinsider/C-Programming-Example)


Projects
--------

* [CMake](https://cmake.org/)
* [CMake projects in Visual Studio](https://docs.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170)
* [Light-City/CPlusPlusThings](https://github.com/Light-City/CPlusPlusThings)
* [libcpr/example-cmake-fetch-content](https://github.com/libcpr/example-cmake-fetch-content)


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




### Youtube

* [Welcome to C++ (The Cherno))](https://youtu.be/18c3MTX0PK0?si=RFc4TAS66zwiJy1H)


### Misc

* [Best C++ Documentation](https://obiztools.com/best-c-documentation/)
* [What is a simple C or C++ TCP server and client example? [closed]](https://stackoverflow.com/questions/662328/what-is-a-simple-c-or-c-tcp-server-and-client-example)
* [Beej's Guide to Network Programming](https://www.beej.us/guide/bgnet/html/)



### TCP And Networking

* [bozkurthan/Simple-TCP-Server-Client-CPP-Example](https://github.com/bozkurthan/Simple-TCP-Server-Client-CPP-Example)

* [Creating a TCP Server in C++](https://www.youtube.com/watch?v=WDn-htpBlnU)
* [ Creating a TCP Client in C++ [Linux / Code Blocks] ](https://www.youtube.com/watch?v=fmn-pRvNaho)

* [Networking in C++s](https://www.youtube.com/watch?v=jS9rBienEFQ)
* [ValveSoftware/GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets)
* [TheCherno/Walnut-Chat](https://github.com/TheCherno/Walnut-Chat)
* [StudioCherno/Walnut-Networking](https://github.com/StudioCherno/Walnut-Networking)
* [StudioCherno/Walnut](https://github.com/StudioCherno/Walnut)

* [TCP Client Server Application | C++ in 2021 ](https://www.youtube.com/watch?v=DVMHEDhYEr4)
* [ C++ Network programming: Basic TCP echo server tutorial ](https://www.youtube.com/watch?v=CFe5LQOPdfk)
* [toprakkeskin/Cpp-Socket-Simple-TCP-Echo-Server-Client](https://github.com/toprakkeskin/Cpp-Socket-Simple-TCP-Echo-Server-Client)
* [Winsock echo server port](https://stackoverflow.com/questions/31461531/winsock-echo-server-port)
* [mafintosh/echo-servers.c](https://github.com/mafintosh/echo-servers.c)

* [Winsock Server Source Code](https://learn.microsoft.com/en-us/windows/win32/winsock/complete-server-code)
* [WSK TCP Echo Server](https://learn.microsoft.com/en-us/samples/microsoft/windows-driver-samples/wsk-tcp-echo-server/)
* [Complete Winsock Client Code](https://learn.microsoft.com/en-us/windows/win32/winsock/complete-client-code)
* [getaddrinfo function (ws2tcpip.h)](https://learn.microsoft.com/en-us/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfo?redirectedfrom=MSDN)


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