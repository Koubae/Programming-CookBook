Ansible 
========

- [ansible.com](https://www.ansible.com/)
- [Getting Started](https://www.ansible.com/resources/get-started?hsLang=en-us)
- [ansible-examples](https://github.com/ansible/ansible-examples)


Documentation
-------------

- [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)

- [Playbooks](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
- [launchpad](https://github.com/techno-tim/launchpad)

- [Inventory]()
  - [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

- [Templating (Jinja2)](https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html#playbooks-templating)


### VM | Virtual Machine 

- [Deploy a virtual machine from a template](https://docs.ansible.com/ansible/2.6/vmware/scenario_clone_template.html)
- [Automate virtual machine deployment with Ansible: Automation](https://www.redhat.com/sysadmin/deployment-ansible-automation)
- [vmware_guest – Manages virtual machines in vCenter](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_module.html)
- [From ISO to Application VM — Using Packer, Ansible and Jenkins to automate VM delivery](https://medium.com/@tpage/from-iso-to-application-vm-using-packer-ansible-and-jenkins-to-automate-vm-delivery-3be709f5c57)
- [Orchestrating Virtual Machines using Ansible and libvirt](https://www.alexandrostheodotou.com/orchestrating-virtual-machines-ansible-libvirt.html)
- [Automating KVM Virtualization](https://nbailey.ca/post/kvm-ansible-automation/)
- [ansible-qemu-kvm](https://github.com/noahbailey/ansible-qemu-kvm)



-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------

### General 

- [Understanding DevOps](https://www.redhat.com/en/topics/devops)


### Ansible

- [Playbook Keywords](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#playbook-keywords)
- [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#yaml-syntax)
- [Modules](https://docs.ansible.com/ansible/latest/user_guide/modules.html#working-with-modules)
- [Patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html#intro-patterns)

- [how to use ansible to deploy docker containers on debian 11](https://www.hostafrica.co.za/blog/linux/ansible-docker-debian-11/)

### Connection and SSH

- [Connection methods and details](https://docs.ansible.com/ansible/latest/user_guide/connection_details.html)

-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------



- Control node ---> the host on which you use Ansible to execute tasks on the managed nodes
- Managed Node --->  a host that is configured by the control node 
- Host inventory ---> a list of managed nodes
- Ad-hoc command ---> a simple one-off task
- Playbook      ----> a set of repeatable tasks for more complex configurations
- Module    -----> code that performs a particular common task such as adding a user, installing a package, etc.
- Idempotency ----> an operation is idempotent if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions


-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----