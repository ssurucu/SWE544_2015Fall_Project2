import socket # Import socket module
from thread import *
from PyQt4 import QtCore, QtGui, uic
from random import randint

class Ticket():
    generatedTicket = [[0 for x in range(5)] for x in range(3)]
    # The class "constructor" - It's actually an initializer
    def __init__(self):

        print ""
        for num in range(0,5) :
            self.generatedTicket[0][num] = randint(0,99)
        for num in range(0,5) :
            self.generatedTicket[1][num] = randint(0,99)
        for num in range(0,5) :
            self.generatedTicket[2][num] = randint(0,99)

        #print generatedTicket[0][0]
        #print generatedTicket[2][2]

    def __getitem__(self, generatedTicket):
        return self.generatedTicket

class User(object):
    username = ""
    addr = 0
    assignedTicket = Ticket()[0]

    # The class "constructor" - It's actually an initializer
    def __init__(self, username, addr):
        self.name = username
        self.addr = addr
        #self.major = assignedTicket



s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name

port = 12345 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
print 'Waiting for connections'
s.listen(5) # Now wait for client connection.


def clientthread(conn):
    #Sending message to client
    conn.send('Welcome to the server.')

    user1 = User("sdsad",3234)

    print user1.assignedTicket[0][0]
    print user1.assignedTicket[1][1]
    print user1.assignedTicket[2][2]


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