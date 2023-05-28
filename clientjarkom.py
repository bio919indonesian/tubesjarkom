#TUGAS BESAR JARINGAN KOMPUTER - KELOMPOK 8 - IF4501
# EKFA EDIET HAMARA (1301213360) - HASNA RAFIDA ALYA (1301213061) - NAUFAL YAZID ZACHARY (1301213001)


import socket #mengimport socket

# Buat socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Baris ini membuat soket klien, yang disebut clientSocket. Parameter pertama menunjukkan keluarga alamat; 
#khususnya, AF_INET menunjukkan bahwa jaringan yang mendasarinya menggunakan IPv4. Parameter kedua menunjukkan bahwa soket bertipe SOCK_DGRAM, 
#yang berarti soket tersebut adalah soket TCP (bukan soket UDP)

# Tentukan alamat server dan port
server_address = ('localhost', 8000) #menetapkan alamat server ke string ‘localhost’ dan mengatur sever port variable integer ke 8000


try:
    # Terhubung ke server
    client_socket.connect(server_address) #menghubungkan soket klien (client socket) ke alamat server yang ditentukan.
    print('Terhubung ke server', server_address)
    
    # Mengiirim permintaan GET ke server
    request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n' #membangun permintaan (request) HTTP yang akan dikirimkan kepada soket server.
    client_socket.sendall(request.encode('utf-8')) 
    #mengirimkan data permintaan (request) kepada soket klien melalui koneksi jaringan setelah mengubahnya menjadi bentuk byte.

    # Menerima response dari server
    response = client_socket.recv(1024)#menerima data dari soket klien (client socket) melalui koneksi jaringan dan menyimpannya dalam variabel response.
    print('Response diterima:') #mencetak “Respinse diterima”
    print(response.decode('utf-8'))#mencetak data yang diterima dari soket klien dalam bentuk string dengan encoding UTF-8.

finally:
    # Menutup koneksi socket
    client_socket.close() #Baris terakhir ini menutup soket dan, karenanya, menutup koneksi TCP antara klien dan server. 
    #Ini menyebabkan TCP di klien mengirim pesan TCP ke TCP di server.
