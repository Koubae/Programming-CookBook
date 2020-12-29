C Installation
==============


Linux | Ubuntu
--------------

See [here](https://github.com/Koubae/Programming-CookBook/tree/master/Linux/Ubuntu#install-cc-compiler)

Linux | Cygwin
--------------

See [here](https://en.wikibooks.org/wiki/C_Programming/Obtaining_a_compiler)

Windows 
-------

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