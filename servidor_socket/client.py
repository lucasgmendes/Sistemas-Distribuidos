#client.py

#!/usr/bin/python                      # This is client.py file

import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.

print("conectando-se ao servidor")
s.connect((host, port))

data = s.recv(1024)
print(data.decode())

x = input("Digite mensagem:")
while(x != 'SAIR'):
    s.send(x.encode())
    print("Mensagem enviada")
    print("Esperando resposta")

    data = s.recv(1024)
    print("Resposta recebida: {}".format(data.decode()))

    x = input("Digite mensagem:")
    
print('Desconectado.')
s.send('SAIR'.encode())
s.close()                              # Close the socket when done

