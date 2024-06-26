import socket
import threading

IP = '192.168.1.72'
PORT = 5555

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(clinet_soket):
    with clinet_soket as sock:
        request = sock.recv(1024)
        print(f'[*] Recived: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()