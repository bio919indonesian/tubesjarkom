#TUGAS BESAR JARINGAN KOMPUTER - KELOMPOK 8 - IF4501
# EKFA EDIET HAMARA (1301213360) - HASNA RAFIDA ALYA (1301213061) - NAUFAL YAZID ZACHARY (1301213001)

import socket #mengimport socket

# Socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Membuat objek baru dimana AF_INET: alamat berbasis pada IPv4 dan SOCK_STREAM: socket TCP

# Bind alamat dan port
server_address = ('', 8000)  #Menggunakan alamat localhost dan port 8000
server_socket.bind(server_address) #Menghubungkan alamat IP dengan nomor port ke socket

# Listen koneksi masuk
server_socket.listen(1) #server menerima koneksi

print('Server berjalan di http://localhost:8000') #mencetak'Server berjalan di http://localhost:8000'

while True:
    # Menunggu koneksi masuk
    print('Menunggu koneksi...') #menampilkan string “Menunggu koneksi…”
    client_socket, client_address = server_socket.accept() #menerima koneksi yang akan masuk untuk membuat koneksi TCP baru dari klien 
    #yang akan mengembalikan sock_client(Objek baru untuk mengirim dan menerima data selama terhubung) dan client_address(alamat klien)

    try:
        print('Menerima koneksi dari', client_address) #mencetak Menerima koneksi dari' client_address

        # Menerima data dari client
        data = client_socket.recv(1024) #utuk menerima data dari soket klien (client socket) melalui koneksi jaringan dengan ukuran maksimum data sebesar 1024 byte.
        request = data.decode('utf-8') #mengubah data yang diterima dari bentuk byte menjadi bentuk string dalam format UTF-8
        print('Data diterima:', request) #mencetak “Data telah diterima” dari soket klien.

        try:
            # Buka file HTML
            with open('index.html', 'r') as file:  #membuka file dengan nama 'index.html' dalam mode membaca ('r')
                content = file.read() #membaca seluruh isi file yang telah dibuka dan disimpan dalam variabel content

        except FileNotFoundError: #menangani kesalahan yang terjadi jika file yang diinginkan untuk dibuka tidak ditemukan
            # Kirim respons "File Not Found"
                response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nFile Not Found\n\n\n\n\n\n File tidak tersedia di Server\n' 
                # variabel ‘response’ merupakan sebuah string yang berisi respon HTTP yang akan dikirimkan sebagai tanggapan atas permintaan yang diterima oleh server
                #respon diatas menampilkan bahwa halaman atau file yang diminta tidak ditemukan (404 Not Found)
                client_socket.sendall(response.encode('utf-8')) 
                #untuk mengirimkan respons HTTP yang telah dikodekan ke dalam byte melalui soket klien kepada klien yang meminta respon tersebut.
                print(response) #menampilkan isi variable ‘response’

        else:
            # Kirim response ke client
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content #membangun respons HTTP yang akan dikirimkan sebagai balasan dari server.
            client_socket.sendall(response.encode('utf-8')) #mengirimkan respons HTTP yang telah dibangun (dalam bentuk string) kepada soket klien melalui koneksi jaringan.

    finally:
        # Tutup koneksi
        client_socket.close() #baris ini menutup soket.
    
# Tutup Socket Server
server_socket.close() #proses kemudian berakhir.
