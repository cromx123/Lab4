import socket
import sys

# Creacion del socket TCP
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definicion del servidor y del puerto de comunicacion
host = 'localhost'
port = 5555

# Conectando el socket al puerto donde el server esta escuchando
server_address = ((host, port))
print("Solicitud Enviada..")
stream_socket.connect(server_address)

# Envia solicitud de datos al servidor
solicitud = 'Solicitud de inscripcion'
stream_socket.sendall(solicitud.encode('utf-8'))

# Recibe la posicion de incripcion del servidor
estado = stream_socket.recv(64)
if estado == b'aceptado':
    data = stream_socket.recv(64)
    print(f"{data}\n")
    
    solicitud2 = 'Solicitud de fecha y hora del curso'
    stream_socket.sendall(solicitud2.encode('utf-8'))
    print("Solicitud Fecha/hora Enviada..")
    consulta = stream_socket.recv(64)
    print(f"{consulta}\n")
else:
    data = stream_socket.recv(64)
    print(data)

      
print('socket cerrado')
stream_socket.close()
