import socket

ip_address_server = input(str("IP Address Server: "))
port = int(input (str("Port: ")))

sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.connect((ip_address_server, port))

request = input(str("Kirim pesan ke server: "))
sock_client.send(request.encode())

response = sock_client.recv(1024)
print("Balasan pesan dari server: " +response.decode())

sock_client.close()
