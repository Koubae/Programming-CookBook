Ansible 
========

- [libvirt](https://libvirt.org/)

Documentation
-------------

- [Ubuntu libvirt](https://ubuntu.com/server/docs/virtualization-libvirt)
- [kvm](https://wiki.ubuntu.com/kvm)  | [kvm installation Ubuntu](https://help.ubuntu.com/community/KVM/Installation)
- [How to get started with libvirt on Linux](https://rabexc.org/posts/how-to-get-started-with-libvirt-on)
- [QEMU/KVM/HVF hypervisor driver](https://libvirt.org/drvqemu.html#xmlconfig)
- [Linux Hypervisor Setup (libvirt/qemu/kvm)](https://octetz.com/docs/2020/2020-05-06-linux-hypervisor-setup/)
- [20.21. EXAMPLE DOMAIN XML CONFIGURATION](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/virtualization_administration_guide/section-libvirt-dom-xml-example)
- [14.9.3. MANIPULATING THE LIBVIRT-GUESTS CONFIGURATION SETTINGS](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/virtualization_administration_guide/sub-sect-shutting_down_rebooting_and_force_shutdown_of_a_guest_virtual_machine-manipulating_the_libvirt_guests_configuration_settings)

- https://docs.fedoraproject.org/en-US/Fedora/18/html/Virtualization_Administration_Guide/form-Virtualization-Managing_guests_with_virsh-Creating_a_virtual_machine_XML_dump_configuration_file.html
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-domain_commands-creating_a_virtual_machine_xml_dump_configuration_file

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------

- [host port forward with qemu through libvirt in user-mode networking](https://serverfault.com/questions/890520/host-port-forward-with-qemu-through-libvirt-in-user-mode-networking)
- [port forwarding with libvirt](https://serverfault.com/questions/720153/port-forwarding-with-libvirt)
- [Running QEMU with port redirection through libvirt](https://snippets.webaware.com.au/howto/running-qemu-with-port-redirection-through-libvirt/)
- [Tip: Find the IP address of a virtual machine](https://rwmj.wordpress.com/2010/10/26/tip-find-the-ip-address-of-a-virtual-machine/)
- [Managing KVM virtual machines part II – the libvirt toolkit](https://leftasexercise.com/2020/05/18/managing-kvm-virtual-machines-part-ii-the-libvirt-toolkit/)
- [Managing KVM virtual machines part III – using libvirt with Ansible](https://leftasexercise.com/2020/05/22/managing-kvm-virtual-machines-part-iii-using-libvirt-with-ansible/)
- [Managing KVM virtual machines part I – Vagrant and libvirt](https://leftasexercise.com/2020/05/15/managing-kvm-virtual-machines-part-i-vagrant-and-libvirt/)


These are the key tools/services/features that enable vitalization.

<ul>
<li><strong><a href="https://www.linux-kvm.org/page/Main_Page">kvm</a></strong>:
<ul>
<li>Kernel-based Virtual Machine</li>
<li>Kernel module that handles CPU and memory communication</li>
</ul>
</li>
<li><strong><a href="https://www.qemu.org">qemu</a></strong>:
<ul>
<li>Quick EMUlator</li>
<li>Emulates many hardware resources such as disk, network, and USB. While it can
emulate CPU, you'll be exposed to qemu/kvm, which delegates concerns like
that to the KVM (which is <a href="https://en.wikipedia.org/wiki/Hardware-assisted_virtualization">HVM</a>).</li>
<li>Memory relationship between qemu/kvm is a little more complicated but can
be <a href="https://www.linux-kvm.org/page/Memory">read about here</a>.</li>
</ul>
</li>
<li><strong><a href="https://libvirt.org">libvirt</a></strong>:
<ul>
<li>Exposes a consistent API atop many virtualization technologies. APIs are
consumed by client tools for provisioning and managing VMs.</li>
</ul>
</li>
</ul>

These tools can be interacted with by users / services.

<ul>
<li><strong><a href="https://libvirt.org/manpages/virsh.html">virsh</a></strong>
<ul>
<li>Command-line tools for communicating with libvirt</li>
</ul>
</li>
<li><strong><a href="https://virt-manager.org">virt-manager</a></strong>
<ul>
<li>GUI to manage KVM, qemu/kvm, xen, and lxc.</li>
<li>Contains a <a href="https://en.wikipedia.org/wiki/Virtual_Network_Computing">VNC</a>
and
<a href="https://en.wikipedia.org/wiki/Simple_Protocol_for_Independent_Computing_Environments">SPICE</a>
client for direct graphical access to VMs.</li>
<li>GUI alternative to <code>virsh</code>, albeit less capable.</li>
</ul>
</li>
<li><strong><a href="https://linux.die.net/man/1/virt-install">virt-install</a></strong>
<ul>
<li>Helper tools for creating new VM guests.</li>
<li>Part of the <code>virt-manager</code> project.</li>
</ul>
</li>
<li><strong><a href="https://linux.die.net/man/1/virt-viewer">virt-viewer</a></strong>
<ul>
<li>UI for interacting with VMs via VNC/SPICE.</li>
<li>Part of the <code>virt-manager</code> project.</li>
</ul>
</li>
</ul>

These tools are used to support the system tools listed above.


<ul>
<li><code>dnsmasq</code>: light-weight DNS/DHCP server. Primarily used for allocating IPs to
VMs.</li>
<li><code>dhclient</code>: used for DHCP resolution; probably on your distro already</li>
<li><code>dmidecode</code>: prints computers SMBIOS table in readable format. Optional
dependency, depending on your package manager.</li>
<li><code>ebtables</code>: used for setting up NAT networking the host</li>
<li><code>bridge-utils</code>: used to create bridge interfaces easily. (tool has been
[deprecated since 2016}(<a href="https://lwn.net/Articles/703776),">https://lwn.net/Articles/703776),</a> but still used)</li>
<li><code>openbsd-netcat</code>: enables remote management over SSH</li>
</ul>

-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------



-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----