# Set of commands (mainly linux but could be Windows / MAC too) relative to C

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


# ------------------ < Compiler > ------------------ #
#  standard conformance
# -std=c90 can also be spelled -ansi, -std=c89, or -std=iso9899:1990.
# Read more -> https://stackoverflow.com/a/14737642/13903942
-std=c90 -pedantic
-std=c99 -pedantic
-std=c11 -pedantic

# simple compilation
gcc main.c -o main 
# Specific version compilation
gcc main.c -std=c17 -o main 


# compile with compiler warning message
# The option -Wall enables all compiler’s warning messages. This option is recommended to generate better code. 
gcc -Wall main.c -o main 
# Generate compiler intermediate files, good for compilation
gcc -Wall -save-temps main.c –o main 