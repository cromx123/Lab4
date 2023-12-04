import socket
import sys

# Creacion del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket al puerto
host = 'localhost'
port = 10000

server_address = (host, port)
print("Iniciando en {} en el puerto {}".format(*server_address))

sock.bind(server_address)
Datos="Soy un libro"
archivo_en_uso= False

while True:
    print("\n Esperando la recepcion del mensaje")
    data, address = sock.recvfrom(4096)
    print(data)
    
    if data == b"dame Datos":
        if not archivo_en_uso:
            archivo_en_uso = True
            sent = sock.sendto(Datos.encode(), address)
        else:
            sent = sock.sendto(b"El archivo esta ocupado por otro usuario", address)
            
    elif data == b"Listo":
        archivo_en_uso = False
        print("Archivo Liberado")