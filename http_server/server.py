import socket
import errno

HEADER_LENGTH_BUFFER = 120
IP = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()


def read_content(client_sock):
    header_buffer = ''
    while True:
        try:
            data = client_sock.recv(500)
            if not data:
                break
            header_buffer += data.decode()
        except Exception as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                return header_buffer


while True:
    client_socket, addr = server_socket.accept()
    client_socket.setblocking(False)
    content = read_content(client_socket)
    print(content)
