# --------------------
#    Installation
# --------------------
sudo apt update
# depen
sudo apt install software-properties-common
# install ansible repo
sudo apt-add-repository --yes --update ppa:ansible/ansible
# install ansible 
sudo apt install ansible 

# Vetify version
ansible --version 


# install sshpass
sudo apt install sshpass 

# --------------------
#    Management
# --------------------
# Copy from source to host destinations
ansible all -m copy -a 'src=dvd.repo dest=/etc/yum.repos.d owner=root group=root mode=0644' -b
# what arguments a module requires , for example copy module requires using:
ansible-doc copy

# CHeck xml syntax
ansible-playbook --syntax-check myplaybook.yml

## SSH
# -> https://docs.ansible.com/ansible/latest/user_guide/connection_details.html
# To set up SSH agent to avoid retyping passwords, you can do:
ssh-agent bash
ssh-add ~/.ssh/id_rsa

# Use the bash and source command 
# @credit: https://stackoverflow.com/a/27541856/13903942
- name: source bashrc
  sudo: no   
  shell: . /home/username/.bashrc && [the actual command you want run]

# --------------------
#    Modules
# --------------------
# list of ava modules
ansible-doc -l
ansible-doc -l | wc -l

# --------------------
#    Hosts
# --------------------

# list hosts within a ansible project
ansible all --list-hosts
# by group
ansible <group_name> --list-hosts
# ping the hosts 
ansible all -m ping