Commands
========

*Uncured listed of useful ready-to-use/reminer commands for multi-purpose usage, mainly bash command, cli and stuff like that*                                   

@Linux
-----

```bash
# ----------------------
# General
# ----------------------
# depackage chrome
sudo dpkg -i [google__.deb]
# check if package is installed
dpkg -s libmagic1

# To copy a file from B to A while logged into B:
scp /path/to/file username@a:/path/to/destination
# To copy a file from B to A while logged into A:
scp username@b:/path/to/file /path/to/destination

# copy to clipboard
curl --location 'https://google.com' | xclip -selection clipboard

# cutting from log unique values 
zcat /path/some_log.gz | grep WHAT_TO_LOOK_FOR | cut -d " " -f 3 | uniq -c
some_executable 2>&1 | tee "some_executable_$(date +'%Y-%m-%d_%H-%M-%S').log"

# log name 
echo "some_executable_$(date +'%Y-%m-%d_%H-%M-%S').log"

# SOrt ls
ls -lRt
# if dont need all other stuff
ls -1Rt

# M
ls -l --block-size=M
# MB
ls -l --block-size=MB

# run in background without logging
./executable.bash > /dev/null 2>&1 &
# kill all python process
pkill -9 python

# kill by name 
ps aux | grep process_name | awk '{print $2}' | xargs kill -9

# find defunct 
ps aux |grep process_name
watch -n1 'ps aux |grep process_name'
watch -n1 'ps aux |grep process_name|wc -l'
watch -n1 'ps aux |grep process_name|grep defunc'
watch -n1 'ps aux |grep process_name|grep defunc|wc -l'
watch -n1 'until lsof -i4 -i6 -sTCP:^LISTEN; do sleep 2; done |wc -l '

sudo lsof|awk '{print $1}' 
sudo lsof|awk '{print $1}' | uniq -c
sudo lsof|awk '{print $1}' | sort | uniq -c
sudo lsof|awk '{print $1}' | uniq -c | sort


# stdout
tail -f /proc/<pid>/fd/1
# stderr
tail -f /proc/<pid>/fd/2

# ==============================================================
#  MACHINE & PERFORMANCE
# ==============================================================
# ubuntu version
lsb_release -a
# Empty trash / bin
rm -rf ~/.local/share/Trash/*

# option gives you memory utilization in MBs.
free -m
# option gives you memory utilization in GBs.
free -g
# display RAM type and speed
sudo lshw -c memory
# check disc size
sudo lsblk
df -h
df -hT

# Neofetch is a command-line system information tool
sudo apt install neofetch 
neofetch 

#### TOP
#https://stackoverflow.com/a/34688904/13903942
# You can add filters to top while it is running. Just press the o key and then type in a filter expression.
# For example, to monitor all processes containing the string "java", use the filter expression COMMAND=java.
# You can add multiple filters by pressing o again.
# You can filter by user with u. Clear all filters with =.
top
htop

nautilus # file explorer / finder

# ----------------------
# Memory Swap Space
# ----------------------
# https://unix.stackexchange.com/questions/23072/how-can-i-check-if-swap-is-active-from-the-command-line
# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-swap.html
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html
# https://phoenixnap.com/kb/swap-space#:~:text=Swap%20space%20in%20Linux%20is,used%20and%20prevents%20memory%20errors.
cat /proc/meminfo
cat /proc/swaps
swapon -s
swapon --show
vmstat 

### --------------------------
##  Services
### --------------------------

# services launched at startup
service --status-all
# disable a service
systemctl disable #<service>
systemctl disable apache2

# restart a service
systemctl restart #<service>

# start a service
systemctl start #<service>

# stop a service
systemctl stop #<service>

# list of all services on your machine
service --status-all
# grep all on
service --status-all | grep +
# grep all off
service --status-all | grep -
# all enable service
systemctl list-unit-files | grep enabled
# currently running
systemctl | grep running
#  similar but with --state filter
systemctl list-unit-files --state=enabled

systemctl list-units --type=service --state=running
systemctl list-units --type=service --state=active


# ==============================================================
#  USERS & FOLDERS & TERMINAL
# ==============================================================
whoami
# use sudo to launch a new shell as the user you want; the -u flag lets you specify the username you want:
sudo -u user2 zsh
whoami

# wsl clock  https://askubuntu.com/a/1169203/1166575
# This command gets the latest time from your Windows machine’s RTC and sets the system time to that.
sudo hwclock --hctosys 

# https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
# https://help.ubuntu.com/community/Beginners/BashScripting
# https://www.taniarascia.com/how-to-create-and-use-bash-scripts/
# To add an existing user to a secondary group, use the -a -G options followed the group’s name and the username:  
usermod -a -G [GROUP] [USER]

# Rename user-name https://askubuntu.com/questions/558669/renaming-user-name
#If running as the user to be modified, logout first, then open a console:
#Press Ctrl+Alt+F1
#Otherwise, simply open a new Terminal:
#Press Ctrl+Alt+T exec 

sudo -i
killall -u [oldname]
id [oldname]
usermod -l [newname] [oldname]
groupmod -n [newname] [oldname]
usermod -d /home/[newname] -m [newname]
usermod -c "[full name (new)]" [newname]
id [newname]


# Add directory to path (in current environment)
export [REF_NAME]=[PATH]
# add to path (persistent)
vim ~/.bashrc
export JAVA_HOME=/usr/java/<your version of java>
export PATH=${PATH}:${JAVA_HOME}/bin

JAVA_HOME=/usr/java/<your version of java>
export PATH=${PATH}:${JAVA_HOME}/bin

source ~/.bashrc 

# --------------- < FOLDERS
#  /bin/sh^M: bad interpreter: No such file or directory
sed -i -e 's/\r$//' file.sh
# display readable byte space in dir
du -sh *
du -shc *

# Create global command / Alias
# https://stackoverflow.com/questions/40984142/linux-create-global-command-that-immediately-takes-user-to-certain-directory
alias [ALIAS NAME]="[COMMAND]"

# --------------- < ZIP
zip -r <output_file> <folder_1> <folder_2> ... <folder_n>
# example
zip -r temp.zip Documents

# unzip - zip 
# create folder
mkdir temp_for_zip_extract
# l et's now extract the zip file into that folder:
unzip /path/to/file.zip -d temp_for_zip_extract

bsdtar --strip-components=1 -xvf file.zip

# --------------- < tree
tree -d  -I 'test*|docs|bin|lib|__pycache__' dir_name
tree -d  -I '__pycache__' dir_name

# ----------------------
# @NetWorking
# ----------------------
cat /proc/1/stat

netstat -pant | grep [PORT_N]
# 1 Grep the host by port
netstat -an | grep 3306

telnet <host> <port>

# List all used port
ss -lntu
# List all used port
ss -lntua

sudo lsof -i -P -n | grep LISTEN

traceroute -T -p 9100 <IP address/hostname>
# convert domain => ip
dig +short stackoverflow.com
read _ _ gateway _ < <(ip route list match 0/0); read _ _ _ _ ip _ < <(ip route get $gateway) ; echo $ip


# --------------- 
# powershell 
# --------------- 
Test-NetConnection -ComputerName localhost -Port 8000
Get-NetFirewallRule -DisplayName WS
wsl hostname -i
ifconfig # The inet IP on eth0 entry is your WSL IP.
inet 172.20.5.240

netsh interface portproxy add v4tov4 listenport=<port> listenaddress=0.0.0.0 connectport=<port> connectaddress=<your WSL IP>

```

@ssh 

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem


# rsa should have enough permissions
chmod 600 ~/.ssh/id_rsa

# Add rsa to ssh config
vim ~/.ssh/config
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa

## check ssh login to github
ssh -T git@github.com


git show --show-signature

```


@terminals

```bash
# open a new terminal and execute in background 
gnome-terminal   -e "ls"
 # https://stackoverflow.com/a/42047402/13903942
xterm -hold -e  ls* -lah & ls

```


@Windows
-------


```bash

```

@wsl

```bash
# ------------- WSL 
# https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview
# https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#1-overview
# Windows dir: /mnt/*
# install rsync 
sudo apt install rsync

# terminate distros
wsl --list --verbose # or wsl -l -v 

wsl -t [DISTRO-NAME]
# close all wsl 
wsl --shutdown 
wsl --shutdown <DistroName>
wsl --shutdown Ubuntu-24.04
wsl --shutdown Ubuntu-22.04


# terminate a specific distro: Windows 1903+
wsl -t <DistroName>
# Boot up the default distro (marked with *):
wsl
# Boot up a specific distro:
wsl -d <DistroName>

# list all avaialble distro to install 
wsl --list --online
# Install specific distro
wsl --install -d <DistroName>
wsl --install -d Ubuntu-22.04
wsl --install -d Ubuntu-24.04

# go from windows to wsl  https://askubuntu.com/a/1435516/1166575
cd Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu-18.04


# once install run 
sudo apt update 
sudo apt full-upgrade 

sudo apt install x11-apps
xeyes &
xcalc
# Remove windows bell sound
sudo vim /etc/inputrc # uncomment line 'set bell-style none'
# Remove bell sound vim / vim 
vim ~/.vimrc # write: 'set visualbell'
# Remove bell sound less
vim ~/.profile # go to end and write 'export LESS="$LESS -R -Q"'

# Delete wsl 
# wsl --unregister <distroName> where <distroName> is the name of your Linux distro, which can be seen from the list in the wsl -l command.
wsl --unregister Ubuntu-20.04 
wsl --unregister Ubuntu-22.04

# https://stackoverflow.com/questions/65815011/moving-files-between-different-wsl2-instances
mkdir /mnt/wsl/share
cp -r .ssh /mnt/wsl/share/
ls -lah /mnt/wsl/share/
cp -r  /mnt/wsl/share/.ssh ~

# https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate
# System has not been booted with systemd as init system (PID 1). Can't operate

```

@Mac
-------

* black setup https://black.readthedocs.io/en/stable/integrations/editors.html

Set as mac shortcut OPT + . 

```bash

```


@python
-------

```python
### find where packages are installed
import sys
import site

print(sys.path)  # Shows all directories Python searches for modules
print(site.getsitepackages())  # System-wide packages
print(site.getusersitepackages())  # User-specific packages

# To check the location of a specific installed package:
import module_name
print(module_name.__file__)
```

```bash
### --------------------------
##  pyenv
### --------------------------
# Install with Homebrew
brew update
brew install pyenv

# Add to your shell (add to ~/.zshrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc

# Install Python versions
pyenv install 3.9.7
pyenv install 3.10.0
pyenv install 3.13.5

# Set global/local version
pyenv global 3.9.7
pyenv global 3.13.5

# List available versions
pyenv versions

# Temporary use for current shell session only
pyenv shell 3.11.11
# Or run Python directly with a specific version
pyenv exec python3.9
# Or specify the full version
pyenv exec python --version 3.11.11
# You can also use the full path to the interpreter
~/.pyenv/versions/3.11.11/bin/python

export PYENV_VERSION=3.10; python -m venv ./sub_folder/sub_folder_2/.venv; source ./sub_folder/sub_folder_2/.venv/bin/activate


### --------------------------
##  pipenv
### --------------------------
### pipenv
# https://www.jetbrains.com/help/pycharm/pipenv.html
# https://pipenv.pypa.io/en/latest/
pip --version
# Install pipenv
pip install --user pipenv

# Init pipenv with current python
pipenv install --python=$(which python)
echo PIPENV_VENV_IN_PROJECT=1 >> .env;pipenv install --python=$(which python)

# content-provider
echo PIPENV_VENV_IN_PROJECT=1 >> .env;pipenv install --python=$HOME/.pyenv/versions/3.10.16/bin/python

# Add to path
# 1. Find user's base binary dir
python -m site --user-base
# 2. Add bin to path
export PATH="$PATH:$HOME/.local/bin"
pipenv --version

pipenv lock    # records new requirements to Pipefile.lock
pipenv update  # records new requirements to Pipefile.lock + installs missing dependencies 

### --------------------------
##  pyenv
### --------------------------
## install & create python venv all commands
pyenv install 3.11.12
pyenv global 3.11.12
pyenv versions
# Install environment 
pipenv install --python=$(which python)
# or
pipenv install --python=$HOME/.pyenv/versions/3.11.12/bin/python

### --------------------------
##  poetry
### --------------------------
# install https://python-poetry.org/docs/
curl -sSL https://install.python-poetry.org | python3 -

# vim ~/.zshrc
#poetry
export PATH="$HOME/.local/bin:$PATH"
# ...
# poetry
fpath+=~/.zfunc
autoload -Uz compinit && compinit

# commands
poetry init
poetry add requests
poetry add --dev pytest
poetry install
poetry build
poetry publish

# clean u
poetry env remove python


# poetry + pyenv
poetry env use $(pyenv which python)
pyenv local 3.11.6

poetry config virtualenvs.in-project true



```


**ruff**

```makefile

# Lint the code (show issues, but do not fix)
lint:
	poetry run ruff check .

# Format the code (auto-fix style issues, like Black)
format:
	poetry run ruff format .

# Lint only and fail if anything is wrong (CI-safe)
check-lint:
	poetry run ruff check . --no-fix

# Check formatting only (but don't modify files)
check-format:
	poetry run ruff format --check .

# Apply auto-fixes for all fixable issues
fix-lint:
	poetry run ruff check . --fix

# Combine formatting and linting fixes
fix-all:
	poetry run ruff format .
	poetry run ruff check . --fix

# Print help: shows all enabled rules
ruff-help:
	poetry run ruff rule --select all
```

@OpenAPI
-----

```bash
brew install openapi-generator

# Generate a Python client from the OpenAPI YAML file: bash Copy
openapi-generator generate -i /path/to/your/openapi-spec.yaml -g python -o ./generated-client
# Generate a Node.js client from the OpenAPI YAML file: bash Copy
openapi-generator generate -i /path/to/your/openapi-spec.yaml -g javascript -o ./generated-client

```