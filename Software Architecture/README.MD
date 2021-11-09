Software Architecture
=======================


Components
----------


* **[Load balancing (computing)](https://en.wikipedia.org/wiki/Load_balancing_(computing))


A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase capacity (concurrent users) and reliability of applications. They improve the overall performance of applications by decreasing the burden on servers associated with managing and maintaining application and network sessions, as well as by performing application-specific tasks.

Load balancers are generally grouped into two categories: **Layer 4** and **Layer 7**. 

Layer 4 load balancers act upon data found in network and transport layer protocols *(IP, TCP, FTP, UDP)*. 

Layer 7 load balancers distribute requests based upon data found in application layer protocols such as HTTP.

Requests are received by both types of load balancers and they are distributed to a particular server based on a configured algorithm. Some industry standard algorithms are:

* Round robin
* Weighted round robin
* Least connections
* Least response time


Layer 7 load balancers can further distribute requests based on application specific data such as HTTP headers, cookies, or data within the application message itself, such as the value of a specific parameter.

Load balancers ensure reliability and availability by monitoring the "health" of applications and only sending requests to servers and applications that can respond in a timely manner.

To learn more on load balancing, visit DevCentral.






-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------


* [non-functional requirements (NFRs)](https://en.wikipedia.org/wiki/Non-functional_requirement)
* [Functional requirement](https://en.wikipedia.org/wiki/Functional_requirement)
* [quality of service (QoS)](https://en.wikipedia.org/wiki/Quality_of_service)
* [high availability (HA)](https://en.wikipedia.org/wiki/High_availability)
* [HA and failover guidelines](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GHA_FAILOVER)
* content attack protection (CAP)
* [Content Security Policy (CSP)](https://www.imperva.com/learn/application-security/content-security-policy-csp-header/)
* [Hardware security modules (HSMs)](https://en.wikipedia.org/wiki/Hardware_security_module)
* [Federated identity](https://en.wikipedia.org/wiki/Federated_identity)
    * [OpenID](https://openid.net)
    * [Security Assertion Markup Language SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language)
    * [OAuth](https://en.wikipedia.org/wiki/OAuth#:~:text=OAuth%20(Open%20Authorization)%20is%20an,without%20giving%20them%20the%20passwords.)
* [JSON Web Token JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)


-----------------------------------------------------------------------------------------------------