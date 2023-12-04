import socket
import sys
import time

# Creacion del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket al puerto
host = 'localhost'
port = 10000

server_address = (host, port)
print("Iniciando en {} en el puerto {}".format(*server_address))

message = b"dame Datos"
message2 = b"Listo"

     # Envia datos
print("enviado solitud del archivo Datos")
sent = sock.sendto(message, server_address)
     
#recepcion
print('Esperando a recibir Datos')
data, address = sock.recvfrom(4096)
print(f"Recibido de {data}")

if data ==b"Soy un libro":
    time.sleep(5)
    print("Termine de usar el libro\n")
    sent = sock.sendto(message2, server_address)



    
print("cerrando socket")
sock.close()