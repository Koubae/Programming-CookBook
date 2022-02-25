Internet Architecture
=====================

DNS 
---

### Elements

* [Domain Name System -- DNS --](https://en.wikipedia.org/wiki/Domain_Name_System)
* [Root name server](https://en.wikipedia.org/wiki/Root_name_server)
* [Name Server](https://en.wikipedia.org/wiki/Name_server)
* DNS resolvers
* [Record_caching](https://en.wikipedia.org/wiki/Domain_Name_System#Record_caching)
* wildcard DNS records
* [Domain name registry](https://en.wikipedia.org/wiki/Domain_name_registry)
* [IANA | Internet Assigned Numbers Authority](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority)
* [WHOIS](https://en.wikipedia.org/wiki/WHOIS)
* [RWHOIS](https://en.wikipedia.org/wiki/WHOIS#RWhois)
* [Telnet](https://en.wikipedia.org/wiki/Telnet)
* [RDAP | Registration Data Access Protocol](https://en.wikipedia.org/wiki/Registration_Data_Access_Protocol)
* [DNS Zone](https://en.wikipedia.org/wiki/DNS_zone)
* [Distributed database](https://en.wikipedia.org/wiki/Distributed_database)
* [User Datagram Protocol (UDP) packets](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
* [fully qualified domain names (FQDNs)](https://en.wikipedia.org/wiki/Fully_qualified_domain_name)
* [ICANN](https://www.icann.org)

* [WHOIS Server Lisrt](https://github.com/rfc1036/whois/blob/next/tld_serv_list)
* [whois manpage](https://manpages.debian.org/stretch/whois/whois.1)
* []()


### RFC & Standards

* RFC 1035 
* RFC 1123 
* RFC 2181 
* RFC 5892
* [RFC 3912](https://datatracker.ietf.org/doc/html/rfc3912)





### Projects & Frameworks

* [Marco d’Itri’s rfc1036 whois | --GITHUB--](https://github.com/rfc1036/whois)


### Documentation

* [WHOIS Overview](https://help.dreamhost.com/hc/en-us/articles/216458227-WHOIS-overview)

-----------------------

### WHOIS ICANN Status Code | Extensible Provisioning Protocol (EPP) domain status code

<table >
<tbody><tr>
<th>Status Code
</th>
<th>Description
</th></tr>
<tr>
<td><b>addPeriod</b>
</td>
<td>This grace period is provided after the initial registration of a domain name. If the registrar deletes the domain name during this period, the registry may provide credit to the registrar for the cost of the registration.
</td></tr>
<tr>
<td><b>autoRenewPeriod</b>
</td>
<td>This grace period is provided after a domain name registration period expires and is extended (renewed) automatically by the registry. If the registrar deletes the domain name during this period, the registry provides a credit to the registrar for the cost of the renewal.
</td></tr>
<tr>
<td><b>inactive</b>
</td>
<td>This status code indicates that delegation information (name servers) has not been associated with the domain. The domain is not activated in the <a href="/wiki/DNS" class="mw-redirect" title="DNS">DNS</a> and will not resolve.
</td></tr>
<tr>
<td><b>ok</b>
</td>
<td>This is the standard status for a domain, meaning it has no pending operations or prohibitions.
</td></tr>
<tr>
<td><b>pendingCreate</b>
</td>
<td>This status code indicates that a request to create the domain has been received and is being processed.
</td></tr>
<tr>
<td><b>pendingDelete</b>
</td>
<td>This status code may be mixed with <i>redemptionPeriod</i> or <i>pendingRestore</i>. In such case, depending on the status set in the domain name, otherwise (not combined with other status), the <i>pendingDelete</i> status code indicates that the domain has been in redemptionPeriod status for 30 days and not restored. The domain will remain in this status for several days, after which time the domain will be dropped from the registry database.
<p>Once deletion occurs, the domain is available for re-registration in accordance with the registry's policies.
</p>
</td></tr>
<tr>
<td><b>pendingRenew</b>
</td>
<td>This status code indicates that a request to renew the domain has been received and is being processed.
</td></tr>
<tr>
<td><b>pendingRestore</b>
</td>
<td>This status code indicates that your registrar has asked the registry to restore the domain that was in redemptionPeriod status. Your registry will hold the domain in this status while waiting for your registrar to provide required restoration documentation. If your registrar fails to provide documentation to the registry operator within a set time period to confirm the restoration request, the domain will revert to redemptionPeriod status.
</td></tr>
<tr>
<td><b>pendingTransfer</b>
</td>
<td>This status code indicates that a request to transfer the domain to a new registrar has been received and is being processed.
</td></tr>
<tr>
<td><b>pendingUpdate</b>
</td>
<td>This status code indicates that a request to update the domain has been received and is being processed.
</td></tr>
<tr>
<td><b>redemptionPeriod</b>
</td>
<td>This status code indicates that your registrar has asked the registry to delete the domain. The domain will be held in this status for 30 days. After five calendar days following the end of the redemptionPeriod, the domain is purged from the registry database and becomes available for registration.
</td></tr>
<tr>
<td><b>renewPeriod</b>
</td>
<td>This grace period is provided after a domain name registration period is explicitly extended (renewed) by the registrar. If the registrar deletes the domain name during this period, the registry provides a credit to the registrar for the cost of the renewal.
</td></tr>
<tr>
<td><b>serverDeleteProhibited</b>
</td>
<td>This status code prevents the domain from being deleted. It is an uncommon status that is usually enacted during legal disputes, at your request, or when a redemptionPeriod status is in place.
</td></tr>
<tr>
<td><b>serverHold</b>
</td>
<td>This status code is set by the domain's Registry Operator. The domain is not activated in the <abbr>DNS</abbr>.
</td></tr>
<tr>
<td><b>serverRenewProhibited</b>
</td>
<td>This status code indicates the domain's Registry Operator will not allow your registrar to renew the domain. It is an uncommon status that is usually enacted during legal disputes or when the domain is subject to deletion.
</td></tr>
<tr>
<td><b>serverTransferProhibited</b>
</td>
<td>This status code prevents the domain from being transferred from your current registrar to another. It is an uncommon status that is usually enacted during legal or other disputes, at your request, or when a redemptionPeriod status is in place.
</td></tr>
<tr>
<td><b>serverUpdateProhibited</b>
</td>
<td>This status code locks the domain preventing it from being updated. It is an uncommon status that is usually enacted during legal disputes, at your request, or when a redemptionPeriod status is in place.
</td></tr>
<tr>
<td><b>transferPeriod</b>
</td>
<td>This grace period is provided after the successful transfer of a domain name from one registrar to another. If the new registrar deletes the domain name during this period, the registry provides a credit to the registrar for the cost of the transfer.
</td></tr></tbody></table>

-----------------------------
