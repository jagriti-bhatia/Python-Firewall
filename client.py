import socket

#socket object is created
s = socket.socket()

#port that the connection needs to be established to
port = 12345

#connect to the server on local computer
s.connect(('127.0.0.1', port))

#decode the recieved data from server to get the string
print (s.recv(1024).decode())


#closing the connection
s.close()
