import socket

#socket object is created
s = socket.socket()
print ("Socket successfully created")

#port that the connection needs to be established to
port = 12345

#bind to the port to the socket
s.bind(('', port))
print ("socket binded to %s" %(port))

#socket is in listening mode
s.listen(5)#5 - limit for the queue of incoming connections
print ("socket is listening")

#infinite loop till connection is inturrupted
while True:

  c, addr = s.accept()
  print ('Got connection from', addr )

  c.send('Thank you for connecting'.encode())

  #close the connection
  c.close()

  #break once the connection is closed
  break
