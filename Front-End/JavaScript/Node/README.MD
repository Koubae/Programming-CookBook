Node
=============

- [openjsf.org](https://openjsf.org)

Libraries
=========


Develop
--------

- [nodemon](https://www.npmjs.com/package/nodemon)
- [TypeScript](https://www.npmjs.com/package/typescript)

Web
----

- [browser-sync](https://browsersync.io)

- [Node Fetch](https://www.npmjs.com/package/node-fetch)
- [concat-stream](https://www.npmjs.com/package/concat-stream)
- [BODY](https://www.npmjs.com/package/body)
- [router](https://www.npmjs.com/package/router)



### Testing 

- [https://docs.cypress.io/guides/overview/why-cypress#In-a-nutshell](https://docs.cypress.io/guides/overview/why-cypress#In-a-nutshell)



Documentation
-------------

- [Introduction to Node.js](https://nodejs.dev/learn)
- [Node.js v16.6.1 documentation](https://nodejs.org/api/esm.html)
- [Differences between ES modules and CommonJS](https://nodejs.org/docs/latest-v14.x/api/esm.html#esm_differences_between_es_modules_and_commonjs)
- [Overview of Blocking vs Non-Blocking in NOde](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/)
- [Node.js v14.17.4 documentation](https://nodejs.org/docs/latest-v14.x/api/)
- [Debugging Guide](https://github.com/pirple/The-NodeJS-Master-Class.git)
- [Upstart Intro, Cookbook and Best Practices.](https://upstart.ubuntu.com/cookbook/#environment-variables)


Utils
-----


Deno
-----

- [Deno](https://deno.land)
- [Deno --GITHUB--](https://github.com/denoland/deno)
- [How Node.js Is Addressing the Challenge of Ryan Dahl’s Deno](https://thenewstack.io/how-node-js-is-addressing-the-challenge-of-ryan-dahls-deno/)

- "I/O" refers primarily to interaction with the system's disk and network supported by [libuv.org](https://libuv.org) **libuv is a multi-platform support library with a focus on asynchronous I/O.**

Other
-----

- [Microsoft’s GitHub agrees to buy code-distribution start-up Npm](https://www.cnbc.com/2020/03/16/microsoft-github-agrees-to-buy-code-distribution-start-up-npm.html)

- [What is difference between httpS and http/2?](https://stackoverflow.com/questions/53488601/what-is-difference-between-https-and-http-2)
- [@Barry Pollard](https://stackoverflow.com/a/53489924/13903942)
> HTTP - A protocol used by clients (e.g. web browsers) to request resources from servers (e.g. web servers).

HTTPS - A way of encrypting HTTP. It basically wraps HTTP messages up in an encrypted format using SSL/TLS. The web is moving towards HTTPS more and more and web browsers are starting to put more and more warnings when a website is served over unencrypted HTTP. Unless you have a very good reason not to, use HTTPS on any websites you create now.

Digging into HTTP more we have:

HTTP/1.1 - this was the prevalent format of HTTP until recently. It is a text-based protocol and has some inefficiencies in it - especially when requesting lots of resources like a typical web page. HTTP/1.1 messages can be unencrypted (where web site addresses start http://) or encrypted with HTTPS (where web site address start with https://). The client uses the start of the URL to decide which protocol to use, usually defaulting to http:// if not provided.

HTTP/2 - a new version of HTTP released in 2015 which addresses some of the performance issues by moving away from a text based protocol to a binary protocol where each byte is clearly defined. This is easier to parse for clients and servers, leaves less room for errors and also allows multiplexing. HTTP/2, like HTTP/1.1, is available over unencrypted (http://) and encrypted (https://) channels but web browsers only support it over HTTPS, where it is decided whether to use HTTP/1.1 or HTTP/2 as part of the HTTPS negotiation at the start of the connection.

HTTP/2 is used by about a third of all websites at the time of writing (up to 50% of websites as of Jan 2020, and 67% of website requests). However not all clients support HTTP/2 so you should support HTTP/1.1 over HTTPS and HTTP/2 over HTTPS where possible (I believe node automatically does this for you when using the http module). I do not believe HTTP/1.1 will be retired any time soon. You should also consider supporting HTTP/1.1 over unencrypted HTTP and then redirect to HTTPS version (which will then use HTTP/1.1 or HTTP/2 as appropriate). A web server like Apache or Nginx in front of Node makes this easy.

HTTP/3 - the next version of HTTP, currently under development. It is expected to be finalised in 2020 though it will likely be late 2020 or even 2021 before you see this widely available in web servers and languages like node. It will be built on top of a UDP-based transport called QUIC (rather than the TCP-based protocol that HTTP/1.1 and HTTP/2 are based on top of). It will include part of HTTPS in the protocol so HTTP/3 will only be available over HTTPS.

In short you should use HTTP/1.1 over HTTPS, should consider HTTP/2 as well if easy to implement (not always possible as not quite ubiquitous yet - but getting there) and in future you might be using HTTP/3.

I suggest you get a firm understanding of all of these technologies (except maybe HTTP/3 just yet) if you want to do web development. It will stand you in good stead.


* **What are the MEAN, MERN, and MEVN stacks? **

MEAN, MERN, and MEVN are technology stacks that help people create websites and mobile applications. All three include MongoDB, Express.js (hence why each begins with “ME”), and NodeJS. The primary difference between the MEAN, MERN, and MEVN stacks can be found in the third letter of each acronym. MEAN is a JavaScript stack that relies on the use of Angular for its front-end JavaScript framework, meanwhile, the MERN stack relies on React and its ecosystem. Finally, MEVN relies on Vue.js and its ecosystem. Here’s a more in-depth picture of the elements that make up these stacks: 

MongoDB – A “NoSQL” database used for storing data for a back-end JavaScript application. If your application has users, MongoDB is an example of a database where your user information will be kept.
Express.js – A light backend framework for serving content to the web. If your backend application needs to send information across the Internet, Express provides tools for accomplishing that.
Angular/React/Vue.js – Front-end JavaScript framework
NodeJS –  A JavaScript “runtime environment” used to run JavaScript outside of a browser, such as on a backend server in the cloud.
A big similarity between MERN, MEVN, and MEAN is that they’re all composed of open-source technologies. They also offer protection against Cross-Site Scripting (XSS) attacks, active support and helpful documentation, and user-interface components for building reusable bits of a web app. MEAN, MEVN, and MERN stacks are not complete without a testing suite, for ensuring everything works as intended, as well as support for MVC architecture (or similar)—which is a great way to produce a well-organized codebase. 