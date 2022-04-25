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

# see what IP your virtua
arp -n

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
# connect with password
virt-manager -c qemu+ssh://username@host1.example.org/system



# Virtual Machine Viewer
sudo apt install virt-viewer
# Connect to virt-viewer via 
virt-viewer <guestname>

# --------------------
#    Management
# --------------------

# Loogin via ssh
ssh  user@ip
# Connecti with a rsa file  
ssh -i ~/rsa user@ip

# https://www.cyberciti.biz/faq/how-to-add-ssh-public-key-to-qcow2-linux-cloud-images-using-virt-sysprep/
--ssh-inject vivek:file:/home/vivek/.ssh/id_rsa.pub

# Checkl libvirtd binary is running 
ps u -C libvirtd

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

# Create VM


# --------------------
#    Network
# --------------------

# start network 
virsh net-start default 

virsh -c qemu:///system net-list
virsh -c qemu:///system net-list --all
# optional step to find the name of the network, in this case "network"
sudo virsh net-list

# check IP addresses allocated to each machine
sudo virsh net-dhcp-leases default
virsh net-dhcp-leases default

# Inspect / Change config network
virsh -c qemu:///system net-dumpxml default

#  forever eliminate the default network.
net-undefine default
#  define a new network starting from an .xml file.
net-define file.xml 

net-dumpxml default > file.xml
# edit ---> net-define file.xml.

# Start / Stop A network 

#  to start the default network.
net-start default
# t, to stop the default network, with the ability of starting it again in the future.
net-destroy default
# to automatically start the default network at boot.
net-autostart default

# Start default 
virsh -c qemu:///system net-start default
# have a look at the stystem 
ps faux
ip address show
sudo iptables -nvL
sudo iptables -t nat -nvL


# Connect 
virt-viewer -c qemu:///system Windows10

# Output a guest's XML configuration file with virsh:
virsh dumpxml {guest-id, guestname or uuid}


# Find IP Address | -> https://unix.stackexchange.com/a/458945/448844
virsh domiflist <guest>
ip neigh | grep -i <MAC_ADDRESS> 

# --------------------
#    Guest
# --------------------
# https://octetz.com/docs/2020/2020-05-06-linux-hypervisor-setup/
# https://docs.fedoraproject.org/en-US/Fedora/18/html/Virtualization_Administration_Guide/form-Virtualization-Managing_guests_with_virsh-Creating_a_virtual_machine_XML_dump_configuration_file.html

# Create guest
virsh create vm.xml 

# Open the configuration file
vim /etc/sysconfig/libvirt-guests

# Copy config file to .config + Add owner to current user
sudo cp -rv /etc/libvirt/libvirt.conf ~/.config/libvirt/ &&\
sudo chown $USER ~/.config/libvirt/libvirt.conf