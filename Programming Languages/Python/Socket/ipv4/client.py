# https://docs.python.org/3/library/socket.html

# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostbyname('localhost'), PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))