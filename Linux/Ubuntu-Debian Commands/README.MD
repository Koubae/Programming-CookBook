# Ubuntu & Debian Commands
=======================

-----------------------------------------------------------------------------------------------------
# Credits

- [Source](https://milq.github.io/useful-terminal-commands-ubuntu-debian/#ubuntu_debian_commands)
- [All content created by Manuel Ignacio López Quintero ](https://milq.github.io/)

-----------------------------------------------------------------------------------------------------


# Useful terminal commands in Ubuntu or Debian

**This is a compilation of my Ubuntu and Debian commands I consider useful.**

|||||
|---|---|---|---|
|1. [Navigation](#Navigation)                |7. [Execution](#Execution)          |.13 [File Permissions](#File-Permissions)         |.19 [SVN](#Subversion-(SVN))|
|2. [Help](#Help)                            |.8 [Redirection](#Redirection)      |.14 [Disk and Devices](#Disk-and-devices)         |.20 [FFmpeg](#FFmpeg) |
|3. [File Manipulation](#File-manipulation)  |.9 [Bash Shortcust](#Bash-shortcuts)|.15 [Compression](#Compression-and-decompression) |.21 [Screen](#Screen)|
|4. [File Visualization](#File-visualization)|.10 [APT](#APT)                     |.16 [Net](#Net)                                   |.22 [PDFtk](#PDFtk)|
|5. [File Information](#File-information)    |.11 [Processes](#Processes)         |.17 [Find](#Find)|
|6. [Administration](#Administration)        |.12 [Users](#Users)                 |.18 [Git](#Git)|


## Features


### Navigation

* **pwd** Print name of current/working directory.
* **ls** path List directory contents (definition of path and wildcards in computing).
* **cd** path Change directory.


### Help 


* **man**   => command Display summary information of a command.
* **command --help** => Display short summary information of a command.
* **command -h**   => Another way to display short summary information of a command.
*** info command**  => Display detailed manual of a command. Only works for some commands.

### File manipulation


* **cp source_path destination_path**  => Copy a file.
* **cp -r source_path destination_path** => Copy a directory.
*** mv source_path destination_path** => Move and/or rename files and directories.
* **mkdir path**  => Make empty directories.
* **rm path**  => Remove a file.
* **rm -r path** => Remove a directory.
* **ln source_path destination_path** => Create a hard link of a file.
* **ln -s source_path destination_path** => Create a symbolic link of a file.
* **nano path_text_file Edit a text file** => Nano is a simple text editor.


### File visualization


* **echo 'text'** => Display a line of text.
* **echo $PATH** => Show the content of the variable PATH.
* **cat** => Concatenate files and print on the standard output.
* **head path_file** => Print the first 10 lines of a text file.
* **tail path_file** => Print the last 10 lines of a text file.
* **more path_file** => Visualize the contents of a text file.
* **less path_file** => Visualize the contents of a text file with more features.
* **grep pattern path_file** => Print lines of a text file that match a pattern.
* **locate pattern** => Search and print files and folders that match a pattern: , sudo updatedb.


### File information


* **file path** => Print file type.
* **stat path** => Print detailed information about a file or directory.
* **wc path_file** => Print newline, word, and byte counts of a text file.
* **ldd path_executable** => Print shared library dependencies of a dynamic executable.
* **diff --color path_file_A path_file_B** => Compare two text files line by line.


### Administration 


* **sudo command** => Execute a command as the superuser (enable sudo on Debian).
* **su username** => Change user ID.
* **su** or **su root** => Become superuser.


### Execution 


* **command1 && command2 && commandN** => Execute multiple commands (AND).
* **command &** => Execute a command in the background.
* **./executable** => Run an executable in the current directory that is not in your PATH.
* **bash script.sh** => Run a Bash script (executable with the header #!/bin/bash).
* **echo $?** => To see the exit status of the last program you ran


### Redirection 


* **command_A | command_B** =>Redirect standard output of command A to standard input of command B.
* **command > file** => Redirect standard output of a command to a new file.
* **command 2> file** => Redirect standard error of a command to a new file.
* **command &> file** => Redirect standard or error output of a command to a new file.
* **command >> file** => Append standard output of a command to a file.
* **command 2>> file** => Append standard error of a command to a file.
* **command &&> file** => Append standard or error output of a command to a file.


### Bash shortcuts 


* **Tab** => Autocomplete files, folders, commands, packages, etc.
* **Tab + Tab** => List all available files, folders, commands, packages, etc.
* **↑** => Go to previous command.
* **↓** => Go to next command.
* **Ctrl + R**  => Search through previously used commands.
* **Ctrl + C** => Terminate the current process (SIGINT).
* **Ctrl + Z** => Suspend the current process (SIGTSTP).


### APT 


* **sudo apt-get install ./package.deb** => Install a local .deb package.
* **sudo apt-get install package** => Install a package from the repository.
* **sudo apt-get purge package** => Uninstall a package from the repository.
* **sudo apt-get update** => Resynchronize the package index files from their sources.
* **sudo apt-get upgrade** => Install the newest versions of all packages currently * installed.
* **sudo apt-get dist-upgrade** => Handle changing dependencies with new versions of packages.
* **sudo apt-get autoremove** => Remove packages that are no longer needed.*


### Processes 


* **ps** => Display the running processes of the current terminal of the current user.
* **ps -e** => Display all running processes.
* **pstree** => Show running processes as a tree.
* **kill** => Send a signal to a process.
* **kill -9 PID** => Kill a process given their PID.
* **top** => Dynamic real-time viewer of processes.
* **htop** => Interactive process viewer (install it with **sudo apt-get install htop**).


### Users 


** **id username** => Print real and effective user and group IDs.
** **who** => Print information about users who are currently logged in.
** **whoami** => Print the username associated with the current effective user ID.


### File permissions and ownership 


* **chmod** => Change file mode bits.
* **umask** => Set file mode creation mask.
* **chown** => Change file owner and group.
* **chgrp** => Change group ownership.


###  Disk and devices


* **lsblk** => List block devices.
* **df -H** => Report file system disk space usage.
* **du -hs path_folde**r => Report disk space usage of a folder.
* **sudo mount device_path** => destination_path Mount a filesystem.
* **sudo umount mounted_device_path** => Unmount a filesystem.
* **sudo mkfs.vfat -I /dev/sdx -n NAME && sync** => Format disk x to VFAT.
* **sudo mkfs.vfat -I /dev/sdxY -n NAME && sync** => Format partition Y from disk x to VFAT.
* **sudo dd bs=512K if=input.iso of=/dev/sdx && sync** => Burn an ISO file to a disk.
* **sudo gdisk /dev/sdx** => GPT editor for disk x (install it with **sudo apt-get install gdisk**).


### Compression and decompression 


* Execute **sudo apt-get install p7zip-full** or **yum install p7zip** => to install 7-Zip.
* **7z x path_zip_file** => Extract a ZIP file.
* **7z x path_iso_file** => Extract an ISO file.
* **7z a filename.zip path_folder** => Compress a directory in a ZIP file.


### Net 

* **ssh user@server** => Log in to a shell of a remote host by SSH.
* **ssh user@server -X** => Log in to a shell of a remote host with X11 forwarding by SSH.
* **scp user@host:path_remote_file path_local** => Copy a file from a remote host to local host.
* **scp path_local_file user@host:path_remote** => Copy a file from a local host to remote host.
* **scp -r user@host:path_folder path_local** => Copy a folder from a remote host to local host.
* **scp -r path_folder user@host:path_remote** => Copy a folder from a local host to remote host.
* **wget URL** => Retrieves a file from the web.
* **wavemon** => Wireless network monitor (install it with sudo apt-get install wavemon).
* **ip** => Show and manipulate routing, network devices, interfaces and tunnels.


### Find 


* **find .** => Find files and folders recursively in current directory.
* **find . -name *.png -exec cp '{}' ~/images \;** => Copy all PNG files to ~/images folder.
* **find . -name *.txt -exec mv '{}' ./txt \;** => Move all TXT files to ./txt folder.
* **find . -name .svn -prune -exec rm -r '{}' \;** => Delete all .svn folders.
* **find . -type f -exec file '{}' \;** => Run files.


### Git 


* Execute **sudo apt-get install git** or **yum install git** => to install Git.
* **git clone uri_repository.git** => Clone a repository into a new directory.
* **git pull** => Incorporates changes from a remote repository into the current branch.
* **git status** => Show the working tree status.
* **git add .** => Update the index using the current content found in the working tree.
* **git commit -m 'message'** => Record changes to the repository.
* **git push** => Update remote references (refs) along with associated objects.


### Subversion (SVN)

* Run **sudo apt-get install subversion** or **yum install subversion** => to install SVN.
* **svnadmin create repository_name** => Create new repository.
* **svn co svn+ssh://user@server/path_to_repository** => Checkout.
* **svn update** => Update working copy.
* **svn status** => Get status of current copy.
* **svn add *** => Add all items recursively.
* **svn add item_name** => Add an item (if folder, adds recursively).
* **svn delete item_name** => Delete an item (if folder, deletes recursively).
* **svn commit -m 'message'** => Commit with log message.


### FFmpeg 

* Run **sudo apt-get install ffmpeg**  => to install FFmpeg.
* **ffmpeg -loop 1 -i 01.png -t 5 out.mp4**  => Convert image to 5 sec. video.
* **ffmpeg -f concat -i mylist.txt -c copy out.mp4**  => Concatenate videos.
* **ffmpeg -r 3 -i %02d.png -r 30 out.mp4**  => 15 images to 30 Hz 5 sec. video.
* **ffmpeg -i input.webm -s 1280x720 out.webm**  => Resize video to 720p.
* **ffmpeg -i in.mp4 -vf 'fade=in:0:25, fade=out:975:25' out.mp4**  => Fade in and out.


### Screen 

* Run **sudo apt-get install screen** or **yum install screen**  => to install Screen.
* **screen**  => Create a screen session.
* **Ctrl + A** then **D**  => Detach from the current screen session.
* **screen -ls**  => List the screen session identification strings.
* **screen -r**  => session_id_string Reattach to a screen session.
* **exit**, or **Ctrl + A then :quit**  => Terminate the current screen session.
* **Ctrl + A then Esc then ↑/↓/PgUp/PgDn**  => Scroll up/down during session.

### PDFtk 

* Run **sudo apt-get install pdftk**  => to install PDFtk.
* **pdftk *.pdf cat output out.pdf**  => Join all PDF files into a new PDF file.
* **pdftk in1.pdf in2.pdf in3.pdf** =>  cat output out.pdf Join 3 PDF files.
* **pdftk in.pdf cat 1 25-35 end output out.pdf**  => Extract pages from a PDF.


-----------------------------------------------------------------------------------------------------