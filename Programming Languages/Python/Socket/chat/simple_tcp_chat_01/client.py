"""
@author: https://www.neuralnine.com/tcp-chat-in-python/
@modified: Federico Bau https://github.com/Koubae/Programming-CookBook
"""
import sys
import socket
import threading
import time

from core import create_tcp_socket, get_machine_host

ENCODING = "ascii"
HOST = get_machine_host()
PORT = 7579

def main():

    username: str = input("Type your username: ")

    client: socket.socket = create_tcp_socket(HOST, PORT, server_type="client")
    app_on: bool = True


    def receive():
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = client.recv(1024).decode(ENCODING)
                if not message:
                    break
                if message == 'NICK':
                    client.send(username.encode(ENCODING))
                else:
                    print(message)
            except BaseException as error:
                print(f"Error occurred (receive) : {error}, closing connection!")
                break

        close_app()

    def send():
        while True:
            try:
                message = f'{username}: {input()}'
                client.send(message.encode(ENCODING))
            except BaseException as error:
                print(f"Error occurred (send) : {error}, closing connection!")
                break
        close_app()

    def run():
        # Starting Threads For Listening And Writing
        receive_thread = threading.Thread(target=receive)
        receive_thread.daemon = True

        write_thread = threading.Thread(target=send)
        write_thread.daemon = True
        receive_thread.start()
        write_thread.start()

    def close_app():
        nonlocal app_on
        app_on = False
        print("Closing the chat , bye!!!")
        client.close()

    def app_teardown(code: int = 0):
        """Perform some clean-up resources, the time sleep are just place-holder and todos """
        time.sleep(1)
        print("Cleaning App Resources...")
        time.sleep(1)
        print("Resources cleaned...")
        time.sleep(1)
        print("App closed ....")
        sys.exit(code)

    try:
        run()
        while app_on:
            time.sleep(1)
        else:
            app_teardown()

    except KeyboardInterrupt as _:
        print(f'[(interrupted by signal 2: SIGINT)] Closing Server ....')
        app_teardown(130)
    except Exception as exception:
        print(f'[{str(exception)}] Exception Occurred Closing Server ....')
        app_teardown(1)
    except BaseException as base_exception:
        print(f'[{str(base_exception)}] Base Exception Occurred Closing Server ....')
        app_teardown(1)




if __name__ == '__main__':
    main()
