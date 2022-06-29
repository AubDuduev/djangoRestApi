import socket

utf8 = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 2000))
server.listen(4)
client_socket, address = server.accept()
data = client_socket.recv(1024).decode(utf8)
print(data, "data")
content = 'Well done....'.encode(utf8)
client_socket.send(content)
print("Server connect")