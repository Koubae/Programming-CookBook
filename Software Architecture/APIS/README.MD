APIs Architecture
================

RESTful Principles
------------------

* Client-server
* Statelessness
* Cacheable
* Layered

### API design Goals

* Affordance
* Loosely  coupled
* Leverage existing web architecture
    * [RFC 2616 protocol](https://tools.ietf.org/html/rfc2616)


### RESTful API Endpoints & Status Codes

Examples:

#### Users
- **POST /users** → Create user → `201 Created` (or `400 Bad Request`)
- **GET /users** → List users → `200 OK`
- **GET /users/{id}** → Get single user → `200 OK` (or `404 Not Found`)
- **PUT /users/{id}** → Replace user → `200 OK` (or `404 Not Found`)
- **PATCH /users/{id}** → Partially update user → `200 OK` (or `404 Not Found`)
- **DELETE /users/{id}** → Delete user → `204 No Content` (or `404 Not Found`)

#### Auth
- **POST /auth/login** → Login → `200 OK` (or `401 Unauthorized`)
- **POST /auth/register** → Register → `201 Created` (or `400 Bad Request`)
- **POST /auth/refresh** → Refresh token → `200 OK` (or `401 Unauthorized`)

#### Items (generic resource)
- **POST /items** → Create → `201 Created`
- **GET /items** → List → `200 OK`
- **GET /items/{id}** → Retrieve → `200 OK` (or `404 Not Found`)
- **PUT /items/{id}** → Replace → `200 OK` (or `404 Not Found`)
- **PATCH /items/{id}** → Partial update → `200 OK`
- **DELETE /items/{id}** → Delete → `204 No Content`

#### Standard HTTP Status Codes
- `200 OK` → Success
- `201 Created` → Resource created
- `204 No Content` → Deleted / no response body
- `400 Bad Request` → Invalid input
- `401 Unauthorized` → Not authenticated
- `403 Forbidden` → Authenticated but not allowed
- `404 Not Found` → Resource missing
- `409 Conflict` → Duplicate / conflicting resource
- `500 Internal Server Error` → Unexpected failure

Components
----------

* API gateway solutions


Guide & Areas of Study
-----------------------


* [ProtoBuf](https://developers.google.com/protocol-buffers/docs/reference/overview)  [Python Generated Code](https://developers.google.com/protocol-buffers/docs/reference/python-generated)
* [AMQP -> Advanced Message Queuing Protocol](https://es.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
* [COAP -> Constrained Application Protocol](https://en.wikipedia.org/wiki/Constrained_Application_Protocol)

* Facade of Microservices, single Entry Point
* Course, Consumer Driven APIs
* Protocol / Data Transformation
* Service Registry and Discovery
* Security and Authorization
* Request Dispatching and Load Balancing
* Orchestration
* Throtting
* Monitoring
