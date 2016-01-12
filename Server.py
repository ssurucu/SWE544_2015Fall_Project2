import socket, threading
from PyQt4 import QtCore, QtGui
from random import randint
import random

host = socket.gethostname()
port = 5000

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []
socketList = []



for t in threads:
    t.join()


class ListenerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        while True:
            tcpsock.listen(4)
            print "\nListening for incoming connections..."
            (clientsock, (ip, port)) = tcpsock.accept()
            newthread = ClientThread(ip, port, clientsock)
            newthread.start()
            threads.append(newthread)
            socketList.append(clientsock)
            #tcpsock.sendall("a user joined")
            #newthread.sendMessageToClient("sssss")



ListenThread = ListenerThread()
ListenThread.start()

class ClientThread(threading.Thread):

    def __init__(self,ip,port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New thread started for "+ip+":"+str(port)


    def run(self):
        # use self.socket to send/receive
        print "Connection from : "+self.ip+":"+str(port)

        self.socket.send("Welcome to the server")

        data = "dummydata"

        while len(data):
            data = self.socket.recv(2048)
            answer = incomingParser(self,data)
            self.socket.send(str(answer))
            #else:
             #   print "Client sent : "+data
             #   self.socket.send("You sent me : "+data)

        print "Client disconnected..."

    def sendMessageToClient(self,message):
        # use self.socket to send/receive
        self.socket.send("sent:" +message)


numberList=set(range(1,99))

def broadcastMessage(message):
    for socket in socketList:
        socket.send("PNA " +str(message))


def getRandomNumberFromStack():
    t = threading.Timer(0.2, getRandomNumberFromStack)
    isGameFinished = False
    if(len(numberList)>0 and not isGameFinished):
        pickedNumber = random.choice(list(numberList))
        numberList.remove(pickedNumber)
        #print(pickedNumber)
        broadcastMessage(pickedNumber)
    else:
        print "Game has finished"
        isGameFinished = True
        t.cancel()
    t.start()

getRandomNumberFromStack()



def incomingParser(self,data):
     #print data
     if data[0:3] == "PNA":
        # Answer with TOC
        self.sendMessageToClient("TOC")
        print data
     if data[0:3] == "TIC":
        # Answer with TOC
        self.sendMessageToClient("TOC")
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
        return checkUserCinko()
     else:
        #conn.send("ERROR")
        print data

def checkUserCinko():
    return "nope, no cinko"