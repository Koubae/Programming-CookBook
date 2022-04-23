# Installations
# kvm  https://wiki.ubuntu.com/kvm | https://help.ubuntu.com/community/KVM/Installation
# make sure Virtualization is on 
# 0 --> no supported
# 1 + ---> Supporeted
egrep -c '(vmx|svm)' /proc/cpuinfo

#To see if your processor is 64-bit, you can run this command:
egrep -c ' lm ' /proc/cpuinfo
#If 0 is printed, it means that your CPU is not 64-bit.
#If 1 or higher, it is. Note: lm stands for Long Mode which equates to a 64-bit CPU.

# Check the Kernel  | x86_64 indicates a running 64-bit kernel
uname -m
# install this 
sudo apt install cpu-checker
# check if kvm can be use
kvm-ok 

# INFO: /dev/kvm exists
# KVM acceleration can be used

# --------------------
#    Installation
# --------------------
sudo apt update
sudo apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils

# Grant Access to login user 
# If the user chosen is the current user, you will need to log out and back in for the new group membership to take effect.
sudo adduser $USER kmv
sudo adduser $USER libvirt

# Verify installation 
virsh list --all

# Install virt-manager (graphical user interface)
# Virtual Machine Manager
sudo apt install virt-manager

# Virtual Machine Viewer
sudo apt install virt-viewer
# Connect to virt-viewer via 
virt-viewer <guestname>

# --------------------
#    Management
# --------------------
# list virtual machine
virsh list

#To start a virtual machine:
virsh start <guestname>

#Similarly, to start a virtual machine at boot:
virsh autostart <guestname>
#Reboot a virtual machine with:
virsh reboot <guestname>
# The state of virtual machines can be saved to a file in order to be restored later. 
# The following will save the virtual machine state into a file named according to the date:
virsh save <guestname> save-my.state
# Once saved the virtual machine will no longer be running.
A saved virtual machine can be restored using:
virsh restore save-my.state
# To shutdown a virtual machine do:
virsh shutdown <guestname>
# A CDROM device can be mounted in a virtual machine by entering:
virsh attach-disk <guestname> /dev/cdrom /media/cdrom
# To change the definition of a guest virsh exposes the domain via
virsh edit <guestname>
