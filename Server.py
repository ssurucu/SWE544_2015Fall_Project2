import socket, threading
from PyQt4 import QtCore, QtGui
from random import randint
import random
import time

host = socket.gethostname()
port = 5000

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []
socketList = []
portList = []
cinkoCount = []
wrongCinkoCount  = []



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
            if(len(socketList)==3):
                time.sleep(3)
                broadcastMessage("GWS Game will start in 3 seconds")
                time.sleep(3)
                assignTickets()
                getRandomNumberFromStack()



ListenThread = ListenerThread()
ListenThread.start()

def incomingParser(self,data,port):
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
        return checkUserCinko(port)
     else:
        #conn.send("ERROR")
        print data



class ClientThread(threading.Thread):
    def __init__(self,ip,port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New thread started for "+ip+":"+str(port)
        portList.append(str(port))



    def run(self):
        # use self.socket to send/receive
        print "Connection from : "+self.ip+":"+str(port)

        self.socket.send("Welcome to the server")

        data = "dummydata"

        while len(data):
            data = self.socket.recv(2048)
            answer = incomingParser(self,data,self.port )
            self.socket.send(str(answer))
            #else:
             #   print "Client sent : "+data
             #   self.socket.send("You sent me : "+data)

        print "Client disconnected..."

    def sendMessageToClient(self,message):
        # use self.socket to send/receive
        self.socket.send("sent:" +message)


numberList=set(range(1,100))
pickedNumberList = []

def broadcastMessage(message):
    for socket in socketList:
        socket.send(str(message))


def getRandomNumberFromStack():
    t = threading.Timer(1, getRandomNumberFromStack)
    isGameFinished = False
    if(len(numberList)>0 and not isGameFinished):
        pickedNumber = random.choice(list(numberList))
        pickedNumberList.append((pickedNumber))
        numberList.remove(pickedNumber)
        #print(pickedNumber)
        broadcastMessage("PNA " + str(pickedNumber))
    else:
        print "Game has finished"
        broadcastMessage("PNA ")
        isGameFinished = True
        t.cancel()
    t.start()

userTickets= []
userTicketArray = []
def assignTickets():
    ticket= []
    for socket in socketList:
        tempTicket = Ticket()
        tempTicketNumbs = tempTicket.getTicket()
        userTickets.append(tempTicketNumbs)
        cinkoCount.append(0)
        wrongCinkoCount.append(0)
        print "tickTemp : " + str(tempTicket.getTicketArray())
        #userTicketArray.append(tempTicketNumbs)
        socket.send("ATI " + str(tempTicketNumbs))

        ticket= []
        ticketRows = tempTicketNumbs.split(";")
        ticketRow0 = ticketRows[0].split(",")
        ticketRow1 = ticketRows[1].split(",")
        ticketRow2 = ticketRows[2].split(",")
        ticket.append(ticketRow0)
        ticket.append(ticketRow1)
        ticket.append(ticketRow2)

        userTicketArray.append(ticket)





    print "tic1" + str(userTicketArray[0])
    print "tic2" + str(userTicketArray[1])
    print "tic3" + str(userTicketArray[2])




broadcastMessage("game will start after 10 secs")
time.sleep(10)



def checkUserCinko(port):
    userIndex = portList.index(str(port))
    if(str(wrongCinkoCount[userIndex])=="3"):
        return "CRB you are banned"
    else:

        #print "USER: "+str(userIndex)


        tempTicket = userTicketArray[userIndex]
        #print "Ticket:" + userTickets[userIndex]
        CinkoPrev = cinkoCount[userIndex]
        CinkoCount = 0
        #print str(CinkoPrev)

        #firstRow
        for num in range(0,5):
            isCinko = False
            for index in range(len(pickedNumberList)):
                if(str(pickedNumberList[index]) == str(tempTicket[0][num])):
                    isCinko = True
            if(isCinko is not True):
                break
        if(isCinko is True):
            print "Cinko 1. sira"
            CinkoCount = CinkoCount + 1


        #firstRow
        for num in range(0,5):
            isCinko = False
            for index in range(len(pickedNumberList)):
                if(str(pickedNumberList[index]) == str(tempTicket[1][num])):
                    isCinko = True
            if(isCinko is not True):
                break
        if(isCinko is True):
            print "Cinko 2. sira"
            CinkoCount = CinkoCount + 1

        #firstRow
        for num in range(0,5):
            isCinko = False
            for index in range(len(pickedNumberList)):
                if(str(pickedNumberList[index]) == str(tempTicket[2][num])):
                    isCinko = True
            if(isCinko is not True):
                break
        if(isCinko is True):
            print "Cinko 3. sira"
            CinkoCount = CinkoCount + 1

        #for index in range(len(pickedNumberList)):
            #print pickedNumberList[index]


        if(str(CinkoCount) == "0"):
            wrongCinko = wrongCinkoCount[userIndex]
            wrongCinkoCount[userIndex] = wrongCinko + 1
            return "CRR"
        else:
            if(str(CinkoPrev) == str(CinkoCount)):
                if(str(wrongCinkoCount[userIndex])=="3"):
                    return "CRB"
                else:
                    return "CRR"
            else:
                return "CRA Hurray Cinko!"

class Ticket():
    generatedTicket = [[0 for x in range(5)] for x in range(3)]
    generatedTicket2 = ""
    # The class "constructor" - It's actually an initializer
    def __init__(self):

        print ""
        a = ""
        for num in range(0,5) :
            self.generatedTicket[0][num] = randint(0,99)
            a=a+str(self.generatedTicket[0][num])+","
        a = a[:-1]

        b = ""
        for num in range(0,5) :
            self.generatedTicket[1][num] = randint(0,99)
            b=b+str(self.generatedTicket[1][num])+","
        b = b[:-1]


        c = ""
        for num in range(0,5) :
            self.generatedTicket[2][num] = randint(0,99)
            c=c+str(self.generatedTicket[2][num])+","
        c = c[:-1]


        self.generatedTicket2 =  ""+ a + ";" + b + ";" + c + ""
        #print generatedTicket[0][0]
        #print generatedTicket[2][2]

    def __getitem__(self, generatedTicket):
        return self.generatedTicket

    def getTicket(self):
        return self.generatedTicket2

    def getTicketArray(self):
        return self.generatedTicket

class UserData():
    # The class "constructor" - It's actually an initializer
    def __init__(self, socket, port, ticket):
        self.socket = socket
        self.port = port
        self.ticket = ticket

        username = ""
        cinkoCount = 0
        wrongCinkoCount = 0