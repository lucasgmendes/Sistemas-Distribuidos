#server.py
#!/usr/bin/python                           # This is server.py file

import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)

while True:
   print('Esperando conexão.')                # Now wait for client connections.
   
   c, addr = s.accept()                    # Establish connection with client.
   print('Conectado', addr)
   c.send('Conectado'.encode())


   print("Esperando mensagem")
   data = c.recv(1024)

   while data.decode() != 'SAIR':
      print('Mensagem recebida: {}'.format(data.decode()))

      x = input("Digite resposta:")
      c.send(x.encode())
      print("Resposta enviada.")

      print("Esperando mensagem")
      data = c.recv(1024)

   c.close()                             # Close the connection
   print('Conexão encerrada.')