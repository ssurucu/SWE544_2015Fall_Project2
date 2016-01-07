import socket # Import socket module
from PyQt4 import QtCore, QtGui, uic

s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

while True:
    data = s.recv(1024)
    print data
    host = raw_input("Please enter hostname: ")


class ClientPlayer():
    def __init__(self, parent=None):
        print "started"

    #Initial functions
    def loginToServer(self,username):
        #this func porvides login to server
        print "server accepted login"

    def quitFromServer(self):
        #this func provides quit from server
        print "server accepted login"

    def listCurrentSessions(self):
        #this func lists current sessions in the server
        print "server accepted login"

    def joinASession(self,sessionname):
        #this func will be used for joining an existing session
        print "server accepted login"

    def createNewSession(self):
        #this func creates a new game session
        print "server accepted login"

    def selectANumber(self):
        #this func will be used for selecting a number
        print "server accepted login"

    def requestCinko(self):
        #this func will be used for selecting a number
        print "server accepted login"

    def learnCinkoStatus(self,username):
        #this func will be used for selecting a number
        print "server accepted login"

    def checkServer(self):
        #this func will send TIC message to check server
        print "server accepted login"


    #this will recognize the messages from the server
    def incomingParser(self, data):
        if data[0:3] == "TIC":
            # Connection ping
            print 'data'
        if data[0:3] == "REJ":
            #User login rejected
            print 'data'
        if data[0:3] == "BYE":
            #User quit
            print 'data'
        if data[0:3] == "LSA":
            #List game sessions
            print 'data'
        if data[0:3] == "JSA":
            #Request to join a game session approved
            print 'data'
        if data[0:3] == "JSD":
            #Request to join a game session declined
            print 'data'
        if data[0:3] == "CSA":
            #Create new game session approved
            print 'data'
        if data[0:3] == "GWS":
            #Session ready, game will start
            print 'data'
        if data[0:3] == "ATI":
            #User is getting the ticket
            print 'data'
        if data[0:3] == "PNA":
            #Randomly picked number announce
            print 'data'
        if data[0:3] == "NSA":
            #User selects number
            print 'data'
        if data[0:3] == "CRA":
            #Cinko requested, cinko is valid
            print 'data'
        if data[0:3] == "CRR":
            #Cinko requested, cinko is invalid
            print 'data'
        if data[0:3] == "CRB":
            #Too many invalid Cinko request, user banned for the session
            print 'data'
        if data[0:3] == "LBA":
            #Learn Cinko status of a user
            print 'data'
        if data[0:3] == "GFA":
            #Game finished, winner username is returned
            print 'data'
        if data[0:3] == "ACI":
            #A user (username) has made a cinko
            print 'data'
        if data[0:3] == "UQU":
            #A user has left the game
            print 'data'
        if data[0:3] == "ERR":
            #Command error
            print 'data'
s.close