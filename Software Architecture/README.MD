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


### Pool 

* [Pool (computer science)](https://en.wikipedia.org/wiki/Pool_(computer_science))

> In computer science, a pool is a collection of resources that are kept in memory, ready to use, rather than the memory acquired on use or the memory released afterwards. 

* [polling (computing)](https://www.techtarget.com/whatis/definition/polling)

> In computer science, polling or a polled operation denotes the process of repeatedly sampling the status of external devices by a client program. The term polling is often used when describing input/output and referred to as software-driven I/O or polled I/O. This process can occur thousands of times a second.

For more information see [Design Principles - Pool](./Design%20Principles/pool.md)

-----------------------------------------------------------------------------------------------------

Testing
--------

* Unit tests
* API validation tests
* Functional tests
* Functional tests
* Load testing
* Runtime error detection tests: Monitoring APIs, Execution errors, Resource leaks, Resource leaks

Security / Authorization
------------------------

*  [OAuth IETF OAuth Working Group](https://tools.ietf.org/wg/oauth/)
* Cross-site scripting (XSS) 
    * Reflected XSS
    * Stored XSS
    * DOM XSS
* [WordPress REST API Bug Could Be Used in Stored XSS Attacks](https://threatpost.com/wordpress-rest-api-bug-could-be-used-in-stored-xss-attacks/124294/)
* DOM XSS
* Cross-site request forgery
* Denial-of-service (DoS)
    * Flood attacks
    * buffer overflow
    * Smurf attacks
    * ping floods
    *  ping of death 

* Distributed denial of service (DDoS)
* Injection attacks
    * Code injection/OS command injection
    * CRLF injection
    * Email (Mail command/SMTP) injection
    * Host header injection
    * LDAP injection
    * SQL injection
    * XPath injection
* IDOR vulnerability
* Man-in-the-middle attacks MITM
    * Sniffing
    * Packet injection
    * Packet injection
    * Email hijacking
    * Wi-Fi eavesdropping
    * Session hijacking
    * Protection measures:  
        * Secure/Multipurpose Internet Mail Extensions (S/MIME)
        * Public key infrastructure (PKI)
        * SSL/TLS certificates
        * System and server configurations
        * HTTP Strict Transport Security (HSTS)

* Replay attacks and spoofing
    * Protection measures:  
        * time-to-live (TTL)
        * MAC implementation onthe client side
        * Kerberos protocol prevention
        * secure routing
        * challenge-handshake authentication protocol (CHAP)


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
* [CI/CD](https://en.wikipedia.org/wiki/CI/CD) | [what-is-cicd](https://www.synopsys.com/glossary/what-is-cicd.html)

* **software layers**: user interface (UI),  Presentation layer, business logic layer, middleware, middleware
* 



 ### Design - Architecture and Patterns

* [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern)
* [Gang of Four design patterns / Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)

-----------------------------------------------------------------------------------------------------