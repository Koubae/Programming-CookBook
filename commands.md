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

# delete all Zone.Identifier
rm -rf **/*Zone.Identifier

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

### Add user 2 in another repo

# create ssh keys
ssh-keygen -t rsa -C "<email.adrrss@example.com>" -f ~/.ssh/id_rsa_koubae

vim ~/.ssh/config

Host github-koubae
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_koubae
    IdentitiesOnly yes


# change the remote so that points to value "Host"
git remote set-url origin git@github-koubae:Koubae/Software-Engineer-Study-Notes.git

# copy key (mac)
pbcopy < ~/.ssh/id_rsa_koubae.pub
# verify (mac)
pbpaste

```

@git

- pull.rebase=true (Always rebase when pulling to avoid merge commits)
- push.autoSetupRemote=true (automatically create remote tracking branches)
- feature.manyFiles=1 (Improved performance for large repository)
- core.fsmonitor=true (Filesystem monitor for improved performance)

```bash
# Clone large projects
# @credti: https://stackoverflow.com/questions/34389446/how-do-i-download-a-large-git-repository
git config --global core.compression 0
git clone --depth 1 <repo_URI>
# multiple times 
git fetch --unshallow
# then pull all at the end
git pull --all

## put core compression back to default if needed
git config --global core.compression -1

git add -p

git commit
#git commit -a
# skip all pre-commit checks
git commit -a --no-verify
git push -u
git push -f

# rebase on latest passing commit from maste
git rebase  -i $(inv circleci.get-latest-passing-master)

git fetch origin master

# rebase
git fetch
git rebase origin/master

### About git amend
# https://stackoverflow.com/questions/179123/how-to-modify-existing-unpushed-commit-messages
git commit --amend
git commit --amend -m "New commit message"
# message + overwrite file
git commit -a --amend -m "My new commit message"


# To amend the previous commit and keep the same log message, run
git commit --amend -C HEAD
# To fix the previous commit by removing it entirely, run
git reset --hard HEAD^
git rebase -i HEAD~commit_count

git push <remote> <branch> --force
# Or
git push <remote> <branch> -f
# n is the number of commits up to the last commit you want to be able to edit (If you want to edit more than one commit message, run)
git rebase -i HEAD~n
#(Replace commit_count with number of commits that you want to edit.) 
# This command launches your editor. 
# Mark the first commit (the one that you want to change) as “edit” # instead of “pick”, 
# then save and exit your editor. Make the change you want to commit and then run
git commit --amend
git rebase --continue


# https://www.notion.so/kraken-tech/Branching-off-a-passing-commit-in-master-36c7eb2f4f434c39a5b5fae79d569d0c
# # Reset head of local master to latest passing commit.
grhm() {
    git checkout master
    current_branch=$(git rev-parse --abbrev-ref HEAD)
    if [ "$current_branch" != "master" ]; then
        echo "You are not on the master branch. Aborting."
        return 1
    fi
    latest_commit=$(inv circleci.get-latest-passing-master)
    git fetch
    git reset --hard $latest_commit
    echo "Reset to $latest_commit"
}

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
# Install Uv
brew install uv

# add to .zshrc
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc

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

# list package size | credit https://stackoverflow.com/a/60850841/13903942
pip list \
  | tail -n +3 \
  | awk '{print $1}' \
  | xargs pip show \
  | grep -E 'Location:|Name:' \
  | cut -d ' ' -f 2 \
  | paste -d ' ' - - \
  | awk '{print $2 "/" tolower($1)}' \
  | xargs du -sh 2> /dev/null \
  | sort -hr


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

### --------------------------
##  inv (Invoke)
# https://www.pyinvoke.org/
### --------------------------
# view available tasks 
inv -l
# tab completition
inv --print-completion-script zsh >> ~/.zshrc
inv --print-completion-script bash >> ~/.bashrc

### --------------------------
##  pycharm
### --------------------------
# indexing process has gotten stuck
# Help → Edit Custom Properties
idea.max.intellisense.filesize=1024
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

@go | @golang
-------

```bash
### Install and manage multiple go versions
go install golang.org/dl/go1.23.0@latest
# Download and install the toolchain
go1.23.0 download
go1.23.0 version
go1.23.0 build
go1.23.0 run main.go

## direnv | https://direnv.net/
# To automatically change go verison
sudo apt install direnv
# vim ~/.bashrc
eval "$(direnv hook bash)"   # for bash
eval "$(direnv hook zsh)"    # for zsh
# vin .envrc
echo 'export PATH=$HOME/go/bin:$PATH' > .envrc
echo 'alias go=go1.23.0' >> .envrc
direnv allow
```

@java
-------

```bash
# Install Java corretto - Add multiple 3 latest versions
# 1) ======================
#    Update system
# 1) ======================
sudo apt update && sudo apt upgrade -y
# 2) ======================
#    Add Amazon Corretto repository
# 2) ======================
# Import the Amazon Corretto GPG key
wget -O- https://apt.corretto.aws/corretto.key | sudo apt-key add -
# Add the repository
sudo add-apt-repository 'deb https://apt.corretto.aws stable main'
# Update package lists
sudo apt update

# 3) ======================
#    Install the latest 3 versions
# 3) ======================
sudo apt install -y java-17-amazon-corretto-jdk
sudo apt install -y java-21-amazon-corretto-jdk
# sudo apt install -y java-22-amazon-corretto-jdk
sudo apt install -y java-24-amazon-corretto-jdk

# 4) ======================
#    Manage multiple Java versions
# 4) ======================
update-alternatives --list java
# Register alternatives (if not auto-registered):
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-17-amazon-corretto/bin/java 1717
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-21-amazon-corretto/bin/java 2121
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-24-amazon-corretto/bin/java 2424

#  Set default Java to the latest (24)
sudo update-alternatives --config java
sudo update-alternatives --display java

java -version

# ======================
#  Set JAVA_HOME
# ======================
# Find your install dir:
ls -d /usr/lib/jvm/java-24-amazon-corretto


# option 2
# Java version switcher
export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
export PATH="$JAVA_HOME/bin:$PATH"

use_java17() {
  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java21() {
  export JAVA_HOME=/usr/lib/jvm/java-21-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java24() {
  export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

# ======================
#  Gradle
# ======================
# Create directory for Gradle
sudo mkdir -p /opt/gradle
cd /opt/gradle

# Download Gradle (replace version if newer is out)
sudo wget https://services.gradle.org/distributions/gradle-8.10.2-bin.zip -P /tmp

# Unzip
sudo unzip -d /opt/gradle /tmp/gradle-8.10.2-bin.zip

# Symlink "current" to latest
sudo ln -sfn /opt/gradle/gradle-8.10.2 /opt/gradle/current

## Add gradle to path
export PATH=/opt/gradle/current/bin:$PATH
source ~/.bashrc
gradle --version

# ======================
#  Maven
# ======================
sudo apt install maven
mvn --version
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

Databases
=========

@PostgreSQL
----------

```bash
# login|connect
psql -h locahost -U admin -d database_name
PGPASSWORD=admin psql -h db-postgres -U admin -d any_business
docker compose exec db-postgres bash -lc "PGPASSWORD=admin psql -h db-postgres -U admin -d any_business"
# connect to db
\c <db-name>
# show database
\l
\l+
SELECT datname FROM pg_database;
# show tables
\d     -- all relations
\d+
\dt
\dv+   -- views
\ds+   -- sequences 
\dt public.*   -- vlist specific schema
\dt schema_name.*   -- vlist specific schema
# show columns
\d tablename
\d+ tablename
\d schema_name.tablename

SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name   = 'users'
ORDER BY ordinal_position;

# enable extension 
CREATE EXTENSION IF NOT EXISTS pgcrypto; 
# create schema
CREATE SCHEMA IF NOT EXISTS myschema;


```


@Snowflake
----------

```bash
# python 
python -m pip install snowflake-connector-python cryptography

# mac
brew install --cask snowflake-snowsql

# key-pair auth

# Generate private key with passphrase (recommended)
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
# Extract the public key
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

# For Snowflake you need Base64 DER of the public key:
#openssl rsa -in rsa_key.pem -pubout -outform DER | base64 -w0 > rsa_key_base64.txt
openssl rsa -in rsa_key.p8 -pubout -outform DER | base64 -w0 > rsa_key_base64.txt

# You’ll now have:
# rsa_key.pem → your private key (keep safe, do not commit)
# rsa_key.pub → human-readable public key
# rsa_key_base64.txt → the version you paste into Snowflake

## paste the keys into ~/.snowsql


# vim ~/.snowsql/config
#[connections.dev]
#accountname = xy12345.eu-west-1
#username = DEV_USER
#private_key_path = /Users/you/rsa_key.pem
#private_key_passphrase = your_passphrase
#role = SYSADMIN
#warehouse = COMPUTE_WH

[connections.dev]
accountname = xy12345.eu-west-1
username = dev_user
private_key_path = ~/.snowsql/rsa_key.p8
role = SYSADMIN
warehouse = COMPUTE_WH

# connect with 
snowsql -c dev
# exit
\q

CREATE USER dev_user
  PASSWORD = 'TEMPORARY_PASSWORD'  -- needed initially
  DEFAULT_ROLE = SYSADMIN
  DEFAULT_WAREHOUSE = COMPUTE_WH
  MUST_CHANGE_PASSWORD = FALSE;

GRANT ROLE SYSADMIN TO USER dev_user;
ALTER USER dev_user SET DEFAULT_ROLE = SYSADMIN;

ALTER USER dev_user
  SET RSA_PUBLIC_KEY = '<paste contents of rsa_key_base64.txt>';


-- See which role Python is using:
-- (from step 1 in Python: CURRENT_ROLE())
-- Then grant visibility to that role:
GRANT USAGE ON DATABASE FAKE_BRONZE_EM TO ROLE MY_PYTHON_ROLE;

-- Also grant schema usage (and object privileges as needed):
GRANT USAGE ON ALL SCHEMAS IN DATABASE FAKE_BRONZE_EM TO ROLE MY_PYTHON_ROLE;
-- and typically:
GRANT SELECT ON ALL TABLES IN SCHEMA FAKE_BRONZE_EM.PUBLIC TO ROLE MY_PYTHON_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA FAKE_BRONZE_EM.PUBLIC TO ROLE MY_PYTHON_ROLE;

GRANT USAGE, OPERATE ON WAREHOUSE COMPUTE_WH TO ROLE SYSADMIN;

# see current session info
SELECT
  CURRENT_ORGANIZATION_NAME() AS org,
  CURRENT_ACCOUNT_NAME()      AS account_name,
  CURRENT_ACCOUNT()           AS account_locator,
  CURRENT_REGION()            AS region,
  CURRENT_USER()              AS user_name,
  CURRENT_ROLE()              AS role,
  CURRENT_SECONDARY_ROLES()   AS secondary_roles;
```