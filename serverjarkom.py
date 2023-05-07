import socket

#server address and port
SERVER_HOST = '127.0.0.1' #alamat lokal
SERVER_PORT = 12345 #port yang digunakan

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_server.bind((SERVER_HOST, SERVER_PORT))

sock_server.listen()

print("Server Ready to launch")

while True:
        sock_client, client_address = sock_server.accept()

        request = sock_client.recv(1024).decode()
        print("Dari Client :" +request)

        response = "Balasan Server :" +request
        sock_client.send(response.encode())

        sock_client.close()
#endwhile
sock_server.close()
                        
