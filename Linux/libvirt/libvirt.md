Ansible 
========

- [libvirt](https://libvirt.org/)

Documentation
-------------

- [Ubuntu libvirt](https://ubuntu.com/server/docs/virtualization-libvirt)
- [kvm](https://wiki.ubuntu.com/kvm)  | [kvm installation Ubuntu](https://help.ubuntu.com/community/KVM/Installation)
- [How to get started with libvirt on Linux](https://rabexc.org/posts/how-to-get-started-with-libvirt-on)
- [Linux Hypervisor Setup (libvirt/qemu/kvm)](https://octetz.com/docs/2020/2020-05-06-linux-hypervisor-setup/)

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------


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