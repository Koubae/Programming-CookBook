Interview Questions
===================


General
------------------


Software Principles
------------------

* [REST](https://en.wikipedia.org/wiki/REST)
* API Design
* Microservice Architecture
* Monolith Architecture
* Distributed Systems and CI/CD
* Event Driven systems | Kafka/message brokers
    * Pub/Sub Architecture
    * Message Queues
* Database Design
* Caching
* Load Balancing
* CDN
* Auth | Security | IAM
* Cybersecurity
    * Cyber Attacks
        * Distributed denial of service (DDoS)

* TCP/IP
* Sockets
* WebSockets 
* HTTP 
* REST
* SOAP
* Long Polling
* Web Hooks

* Scaling | Vertical | Horizontal


Architecture & Design Frameworks
------------------

### SOLID

* S: Single Responsability 
* O: Open-Closed 
* L: Liskov Substitution 
* I: Interface Segregation 
* D: Dependency Inversion

* S: Do one thing (Single responsibility).
* O: Add features without breaking old code (Open/closed).
* L: Subclasses should behave like parents (Liskov).
* I: Small interfaces > big ones (Interface segregation).
* D: Rely on abstractions, not details (Dependency inversion).

### Clean Architecture / Screaming Architecture

* [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html)

source code dependencies can only **point inwards.**

### Hexagonal Architecture 

* [What's Hexagonal Architecture?](https://medium.com/@luishrsoares/whats-hexagonal-architecture-6da22d4ab600)
* [Hexagonal architecture (software)](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))
* Really good --> [Hexagonal Architecture, there are always two sides to every story](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c)
* [DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)

### DDD Domain Driven Design

* [wiki -- Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
* [sso -- What is Domain Driven Design?](https://stackoverflow.com/questions/5325836/what-is-domain-driven-design)

##### HEART Framework

* Happiness
* Engagement
* Adoption
* Retention
* Task Success

-  GSM process: Goals, Signals, Metrics

### Other Architectures

* [EBI Architecture](https://herbertograca.com/2017/08/24/ebi-architecture/)
* [Ports & Adapters Architecture](https://herbertograca.com/2017/09/14/ports-adapters-architecture/)


Testings
-----------

### A/B Testing


- A/B testing is a user experience research methodology. A/B tests consist of a randomized experiment that usually involves two variants, although the concept can be also extended to multiple variants of the same variable
- A/B testing is essentially an experiment where two or more variants of a page are shown to users at random, and statistical analysis is used to determine which variation performs better for a given conversion goal.

In an A/B test, you take a webpage or app screen and modify it to create a second version of the same page. This change can be as simple as a single headline, button or be a complete redesign of the page. Then, half of your traffic is shown the original version of the page (known as control or A) and half are shown the modified version of the page (the variation or B).

More than just answering a one-off question or settling a disagreement, A/B testing can be used to continually improve a given experience or improve a single goal like conversion rate optimization (CRO) over time.

#### A/B testing process

* Collect data
* Identify goals
* Generate test hypothesis
* Create different variations
* Run Experiment
* Analyze Results


* Use rel="canonical":  If you run a split test with multiple URLs, you should use the [rel="canonical"](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) 
* Use 302 redirects instead of 301s

#### A/B Testing metrics

There are three common metrics frameworks you can follow:

* Google’s HEART
* Pirate Metrics (AARRRR) acquisition, activation, retention, referral, and revenue.
* The North Star Metrics framework

* [10 A/B Testing Metrics To Track Results and Measure Success](https://userpilot.com/blog/ab-testing-metrics/)
* [How to Use Google’s HEART Framework to Improve Your SaaS Product](https://userpilot.com/blog/google-heart-framework/)
* [How to choose the right UX metrics for your product](https://library.gv.com/how-to-choose-the-right-ux-metrics-for-your-product-5f46359ab5be)


Databases
------------------

* Sharding
* Write/Read Architecture | Principles


Data Science
------------------

### General

#### Data Point

Data points are building blocks of data analysis
A data point is a discrete unit of information. In a general sense, any single fact is a data point. The term data point is roughly equivalent to ***datum***, the singular form of data.

Data point can help formulate hypothesis.

* [data point](https://www.techtarget.com/whatis/definition/data-point)
* [Optimization: Why Data Points Matter?](https://www.linkedin.com/pulse/optimization-why-data-points-matter-expanz/)


Terminology
----------


- A/B - Testing
- (CRO) Conversion Rate Optimization
- ROI Return on Investment
-  GSM process: Goals, Signals, Metrics
* Pirate Metrics (AARRRR) acquisition, activation, retention, referral, and revenue.
- Data point
- data collections
- datum
- SOLID
- Clean Architecture
- Hexagonal Architecture
- Onion Architecture
- Screaming Architecture
- Domain-Driven Design
- EBI Architecture
- Ports & Adapters Architecture
    - Primary/Driving Adapters  `<-> ()`
    - Secondary/Driven Adapters `() <->`


Videos 
----------

### Youtube

* [System Design Mock Interview: Design TikTok ft. Google TPM](https://www.youtube.com/watch?v=Z-0g_aJL5Fw&t=988s)
* [System Design Mock Interview: Design Facebook Messenger](https://www.youtube.com/watch?v=uzeJb7ZjoQ4)
* [Google system design interview: Design Spotify (with ex-Google EM)](https://www.youtube.com/watch?v=_K-eupuDVEc)

