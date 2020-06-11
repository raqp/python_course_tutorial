import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
print("conn:", conn)
data = conn.recv(1024)
while data:
    conn.send(data.upper())

conn.close()
