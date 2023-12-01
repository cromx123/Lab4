import socket
import sys

#Creacion del socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Definicion del host
host = 'localhost'

#Definicion de puerto de comunicacion
port = 5555

#Vincular el socket al puerto
sock.bind((host, port))

#Escuchando las conexiones entrantes
sock.listen(5)

# Solicitudes posicion
position = 0
# Solicitudes permitidas
max=4
# Datos del Curso
curso = 'El curso se realizara el dia 15 de diciembre a las 9:00hrs.'
#Esperando por conexion
print('Esperando conexiones...')
while True:
    connection,client = sock.accept()
    print("\n")
    print(f'Conexion realizada con {client}')
    position+=1
    
    #Enviar mensaje a cliente
    # Recibir los datos y retransimitirlos
    solicitud = connection.recv(64)
    
    if position < max:
        solicitud = 'aceptado'
        connection.sendall(solicitud.encode('utf-8'))
        
        mess = f'Su solicitud fue aceptada.'
        connection.sendall(mess.encode('utf-8'))
        
        consulta = connection.recv(64)
        if consulta == b'Solicitud de fecha y hora del curso':
            print(f'Recibida {consulta}')
            connection.sendall(curso.encode('utf-8'))
        elif consulta == b'Solicitud de posicion de incripcion':
                print(f'Recibida {consulta}')
                mess2 = f'Su posicion fue {position}'
                connection.sendall(mess2.encode('utf-8'))
                
        consulta2 = connection.recv(64)
        if consulta2 == b'Solicitud de fecha y hora del curso':
            print(f'Recibida {consulta2}')
            connection.sendall(curso.encode('utf-8'))
        elif consulta2 == b'Solicitud de posicion de incripcion':
                print(f'Recibida {consulta2}')
                mess2 = f'Su posicion fue {position}'
                connection.sendall(mess2.encode('utf-8'))
        
    else:
        solicitud = 'rechazado'
        connection.sendall(solicitud.encode('utf-8'))
        
        mess = f'Su solicitud fue rechazada, puesto que el curso ya esta lleno'
        connection.sendall(mess.encode('utf-8'))
        break
        
    
    
    #Cerra la conexion
    print(f'Conexión con {client} cerrada.')
    connection.close()
