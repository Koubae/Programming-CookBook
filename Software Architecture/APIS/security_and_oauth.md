APIs - Security & OAuth
===============


Authorization workflow
----------------------

* **Credit[Hands-On RESTful API Design Patterns and Best Practices](https://www.oreilly.com/library/view/hands-on-restful-api/9781788992664/**

The flow is as follows. The application client first sends a request and grabs a JWT access
token from the third-party authentication and authorization server by supplying the
mandated credentials. Once the mandated credentials are obtained, the client then embeds
the access token in the Authorization HTTP header of the API request. The API
Gateway then validates the access token supplied by the client with the authorization
server. Once validated by the third-party authentication server, the API gateway passes the
JWT access token to the appropriate backend microservices to initiating the business tasks.
If there is a need for other downstream microservices to fulfill the service request, then the
same JWT token is shared across to all the participating and contributing microservices.
Microservices that are in collaborating mode have to attach the JWT access token to their
request messages: 

* Confidentiality / Confidentiality / Availability / Secure communication

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------

*  Distributed denial of service (DDoS)

-----------------------------------------------------------------------------------------------------