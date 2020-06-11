import socket

host = ''
port = 9090
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.sendall(b"Hello Hayk!")
data = sock.recv(1024)
print(data)