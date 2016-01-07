import socket # Import socket module
from thread import *

s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name

port = 12345 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
print 'Waiting for connections'
s.listen(5) # Now wait for client connection.


def clientthread(conn):
    #Sending message to client
    conn.send('Welcome to the server.')

    while True:

        #Receive from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()



while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

    def incomingParser(self, data):
         print data
         if data[0:3] == "TIC":
            # Answer with TOC
            print data
         if data[0:3] == "LOG":
            # User Login
            print data
         if data[0:3] == "QUI":
            # User Quit
            print data
         if data[0:3] == "LSQ":
            # List game sessions
            print data
         if data[0:3] == "JSQ":
            # Join a session
            print data
         if data[0:3] == "CSQ":
            # Create new session
            print data
         if data[0:3] == "SEN":
            # User selects number
            print data
         if data[0:3] == "CIN":
            # Cinko request
            print data