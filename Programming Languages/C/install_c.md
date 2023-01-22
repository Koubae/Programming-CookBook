Install C
==============

- [GCC Releases](https://gcc.gnu.org/releases.html)

In order to start to develop in **C** you should at least install the following:

- **`gcc`:** GNU C Compiler
- **`gdb`:** C debugger

There are different distribution of C, depending on what you need to build. For example, for Windows apps, 
using the IDE [Visual Studio](https://visualstudio.microsoft.com/vs/) (Not [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=DX_841432) which is more of a Editor with IDE capabilities on command)), will use a different C distribution by default more oriented for Windows developement, and Windows set of *C libraries*.
Check out more on [Compilers](#compilers) below.


- [Linux](#linux)
- [Windows](#windows)


Linux
--------------

- [Installing GCC - Download](https://gcc.gnu.org/install/)
- [How to switch between multiple GCC and G++ compiler versions on Ubuntu 20.04 LTS Focal Fossa](https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-20-04-lts-focal-fossa)
- [Linux | Ubuntu (C++)](https://github.com/Koubae/Programming-CookBook/tree/master/Linux/Ubuntu#install-cc-compiler)


### Ubuntu

```bash
sudo apt install build-essential

# ------------------ < Installation > ------------------ #
sudo apt update
sudo apt upgrade
sudo apt -y install gcc 
sudo apt-get install build-essential gdb
gcc --version


# Multiple GCC version https://www.fosslinux.com/39386/how-to-install-multiple-versions-of-gcc-and-g-on-ubuntu-20-04.htm
sudo apt install build-essential
sudo apt -y install gcc-7 gcc-8
sudo add-apt-repository ppa:jonathonf/gcc-9.0
sudo apt-get install gcc-9

```

### Cygwin

- [Linux | Cygwin](https://en.wikibooks.org/wiki/C_Programming/Obtaining_a_compiler)



Windows 
-------

- [Install C/GCC Compiler for Windows DigitalOcean](https://www.digitalocean.com/community/tutorials/c-compiler-windows-gcc)

### MinGW

- [GCC, the GNU Compiler Collection](https://gcc.gnu.org/)

1. Go to [sourceforge.net](https://sourceforge.net/projects/mingw/) download and & this to your hard drive.

2. Once the download is finished, open it and follow the instructions

3. Set your PATH. 
    1. Right-click on "My computer" and click "Properties".
    2. Go to the "Advanced" tab and click on "Environment variables". 
    3. Go to the "System variables" section and scroll down until you see "Path". 
    4. Click on it, then click "edit". 
    5. Add ```;C:\MinGW\bin\``` 
    6. To test if GCC works, open a command prompt and type "gcc". 

NOTE: Add executables to your Windows PATH
``` 
C:\msys64\mingw64\bin
C:\msys64\usr\bin
``` 
Header files and libraries

``` 
# The dynamic lib runtime .dll files will be in bin dirs
# Add the bin directory to PATH environment variable so it can find the .dll files
C:\msys64\mingw64\bin
C:\msys64\usr\bin

# Static libraries
C:\msys64\usr\lib
C:\msys64\mingw64\lib

# Header files
C:\msys64\usr\include
C:\msys64\mingw64\include
``` 


Compilers
---------


### Windows OS Compilers

#### Free

<li>CCS C Compiler</li><li>Turbo C</li><li>Minimalist GNU for Windows (MinGW)</li><li>Portable C Compiler</li><li>Clang C++</li><li>Digital Mars C++ Compiler</li><li>Intel C++</li><li>IBM C++</li><li>Visual C++ : Express Edition</li><li>Oracle C++</li>

#### Payment

<li>Embarcadero C++</li><li>Edison Design Group C++</li><li>Green Hills C++</li><li>HP C++ for Unix</li><li>Intel C++&nbsp;for Windows, Linux, and some embedded systems.</li><li>Microsoft C++</li><li>Paradigm C++</li>


<p>To use the C compiler in Windows, you can install any software mentioned below.</p><ul><li>You can <a href="https://www.microsoft.com/express/download/" rel="nofollow noopener">download a 90-day trial version of Visual Studio</a></li><li>You can download <a href="https://www.bloodshed.net/">Dev-C++ IDE</a> to develop C and C++ applications.</li><li>You can install <a href="http://www.mingw.org/" rel="nofollow noopener">MinGW</a>