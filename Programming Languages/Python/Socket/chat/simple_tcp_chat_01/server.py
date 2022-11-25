"""
@author: https://www.neuralnine.com/tcp-chat-in-python/
@modified: Federico Bau https://github.com/Koubae/Programming-CookBook
"""
import sys
import socket
import threading

from core import create_tcp_socket, get_machine_host

ENCODING = "ascii"
HOST = get_machine_host()
PORT = 7579
MAX_CON = 5

lock = threading.Lock()

def main():

    server: socket.socket = create_tcp_socket(HOST, PORT)
    # the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state,
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.listen(MAX_CON)
    print(f'Server listening at {HOST}:{PORT} ....')

    def run():

        clients = {}

        def broadcast(message: bytes) -> None:
            for client, _ in clients.values():
                client.send(message)

        def receive_client_message(client: socket.socket, nickname: str):

            while True:
                try:
                    message = client.recv(1024)
                    if not message:
                        break
                    print(f'{nickname} Sending Message : {message}')
                    broadcast(message)
                except Exception as error:
                    print(f"{nickname} had an error..  Error {str(error)}")
                    break
            message = f'{nickname} left the chat!'
            print(message)
            broadcast(message.encode(ENCODING))
            client.close()

            with lock:
                del clients[nickname]

        def listen():
            while True:
                # Accept new connections
                client, address = server.accept()
                print(f'New Connection with {str(address)}')

                # Request and store nickname
                client.send("NICK".encode(ENCODING))
                nickname = client.recv(1024).decode(ENCODING)

                # Broadcast new client to chat
                message = f'{nickname} joined the chat!'
                print(message)
                broadcast(message.encode(ENCODING))
                client.send('Connected to the server!'.encode(ENCODING))

                # Register client to a new thread
                thread = threading.Thread(target=receive_client_message, args=(client, nickname))
                thread.daemon = True
                with lock:
                    clients[nickname] = (client, thread)

                thread.start()

        listen()

    try:
        run()

    except KeyboardInterrupt as _:
        print(f'[(interrupted by signal 2: SIGINT)] Closing Server ....')
        sys.exit(130)
    except Exception as exception:
        print(f'[{str(exception)}] Exception Occurred Closing Server ....')
        sys.exit(1)
    except BaseException as base_exception:
        print(f'[{str(base_exception)}] Base Exception Occurred Closing Server ....')
        sys.exit(1)




if __name__ == '__main__':
    main()
