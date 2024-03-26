import socket

target_ip = "192.168.1.72"
target_port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_ip, target_port))

client.send(b'Test')

response= client.recv(4096)

print(response.decode())
client.close()
exit