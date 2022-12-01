# List of command related to Socket programming and TCP


# Find (and kill) process locking port 3000 on Mac [closed] https://stackoverflow.com/q/3855127/13903942
lsof -i tcp:[PORT]
#or also
netstat -vanp tcp | grep 3000


# state
netstat -an | grep [PORT]
lsof -i -n | grep [PORT]


# ping
ping -c 3 127.0.0.1
