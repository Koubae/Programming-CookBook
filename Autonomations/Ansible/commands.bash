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