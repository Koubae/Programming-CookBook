# Ubuntu
=======================



- [Ubuntu Cheatsheet](https://github.com/JREAM/ubuntu-cheatsheet)

- [Useful Ubuntu Commands ](https://gist.github.com/tecoholic/988309/25df7544f1c4e4a8636d60a7ca3224f6e022af88)

## Common


* cd -> Home directory

* pwd -> Check current path

* ls -> Check current folder



## Install C/C++ compiler

```

sudo apt-get update

sudp apt-get install build-essential gdp g++

g++ --version

gdp --version

```


-----------------------------------------------------------------------------------------------------

## VS Code


* Install VS Code

```

sudo apt-get install snap

sudo snap install --classic code 

```

* Start VS Code

```

code .

```

### Set Up VS Code

1 Install C/C++ Microsoft Extension

2 Run > Start Debuggin > C++ GDB/LLDB

3 g ++

4 Should Generate a JSON Configuration



-----------------------------------------------------------------------------------------------------


### Install VirtualBox Guest Additions for Ubuntu.


```
 sudo apt update

 sudo apt upgrade

 sudo apt install build-essential dkms linux-headers-$(uname -r)

```

Then go to Oravle VM > Devices > Insert Guest Additions CD image.

It will automatically install the Guest Addiiont.


Now to enable Shared Clipboard and Drag’n’Drop functionality 
between Guest and Host Machine. Go to General => Advanced and enable the two options 
(Shared Clipboard and Drag’n’Drop) as you wish, from the drop down options. 
Then click OK to save the 
settings and boot your system, login and test if everything is working fine.


#### Mount CDRom in Ubuntu.

sudo su
cd /media
mkdir cdrom
mount /dev/cdrom /media/cdrom
> sudo mount /dev/cdrom /media/cdrom





-----------------------------------------------------------------------------------------------------