import socket # Import socket module
from thread import *
#from PyQt4 import QtCore, QtGui, uic
from random import randint
import random
import threading

class Ticket():
    generatedTicket = [[0 for x in range(5)] for x in range(3)]
    # The class "constructor" - It's actually an initializer
    def __init__(self):

        print ""
        a = "["
        for num in range(0,5) :
            self.generatedTicket[0][num] = randint(0,99)
            a=a+str(self.generatedTicket[0][num])+","
        a = a[:-1]
        a=a+"]"

        b = "["
        for num in range(0,5) :
            self.generatedTicket[1][num] = randint(0,99)
            b=b+str(self.generatedTicket[1][num])+","
        b = b[:-1]
        b=b+"]"


        c = "["
        for num in range(0,5) :
            self.generatedTicket[2][num] = randint(0,99)
            c=c+str(self.generatedTicket[2][num])+","
        c = c[:-1]
        c=c+"]"


        print "["+ a + "," + b + "," + c + "]"
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

numberList=set(range(1,99))

def getRandomNumberFromStack():
    t = threading.Timer(0.2, getRandomNumberFromStack)
    isGameFinished = False
    if(len(numberList)>0 and not isGameFinished):
        pickedNumber = random.choice(list(numberList))
        numberList.remove(pickedNumber)
        print(pickedNumber)
    else:
        print "Game has finished"
        isGameFinished = True
        t.cancel()
    t.start()

socketList = []
sessionUserList = []
def addUserToSession(username,port):
    tempUser = User(username,port)
    sessionUserList.append(tempUser)


def broadcast (server_socket, sock, message):
    for socket in socketList:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in socketList:
                    socketList.remove(socket)





def clientthread(conn):
    #Sending message to client
    conn.send('Welcome to the server.')




    #print str(user1.assignedTicket[0][0]) +" | " +  str(user1.assignedTicket[0][1]) +" | " +  str(user1.assignedTicket[0][2])+" | " +  str(user1.assignedTicket[0][3])+" | " +  str(user1.assignedTicket[0][4])
    #print str(user1.assignedTicket[1][0]) +" | " +  str(user1.assignedTicket[1][1]) +" | " +  str(user1.assignedTicket[1][2])+" | " +  str(user1.assignedTicket[1][3])+" | " +  str(user1.assignedTicket[1][4])
    #print str(user1.assignedTicket[2][0]) +" | " +  str(user1.assignedTicket[2][1]) +" | " +  str(user1.assignedTicket[2][2])+" | " +  str(user1.assignedTicket[2][3])+" | " +  str(user1.assignedTicket[2][4])




    while True:

        #Receive from client

        #getRandomNumberFromStack()
        data = conn.recv(1024)
        reply = 'OK...' + data
        incomingParser(data)
        if not data:
            break

        #conn.sendall(reply)

    #came out of loop
    conn.close()


while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    socketList.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #broadcast("a user Connected with " + addr[0] + ':' + str(addr[1]))
    broadcast(s, conn, "[%s:%s] entered our gaming room\n" % addr)

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))


    def incomingParser(data):
         print data
         if data[0:3] == "TIC":
            # Answer with TOC
            conn.send("TOC")
            print data
         if data[0:3] == "LOG":
            # User Login
            print conn.getpeername()[1]
            #if():

            conn.sendall(data[4:]+" has joined the session")
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
         else:
             conn.send("ERROR")