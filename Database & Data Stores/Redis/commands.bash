# ping server
PING

SET user:1:name "John"
GET user:1:name

# expiration
SET user:2:name "Doe" EX 10
GET user:2:name
# Check remaining TTL
TTL user:2:name

# Atomic Counter
SET page:views 0
INCR page:views
INCR page:views
INCR page:views
GET page:views

# Hashes — objects | Map | Dict
HSET user:1 name "John" username "Doe" email "john.doe@example.com" age 99
HGET user:1 name
# whole hash
HGETALL user:1
# update
HSET user:1 age 35
HGET user:1 age
