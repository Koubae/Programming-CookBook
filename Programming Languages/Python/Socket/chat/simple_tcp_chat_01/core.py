import socket


def get_machine_host() -> str:
    """Short cut to get the default machine host"""
    return socket.gethostbyname(socket.gethostname())


def create_tcp_socket(host: str, port: int, server_type: str = "server") -> socket.socket:
    """
        Creates a simple TCP Socket
    :param host: Host example 127.0.0.1
    :param port: Port example 8080
    :return: A new Socket instance bind with the given (host, port) address
    """
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_type == "client":
        socket_connection.connect((host, port))
    else:
        socket_connection.bind((host, port))
    return socket_connection
