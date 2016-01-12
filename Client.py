import socket # Import socket module
#from PyQt4 import QtCore, QtGui, uic
import json




s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
host = raw_input("Please enter username: ")


while True:
    h = raw_input("cmd: ")
    s.send(h)
    data = s.recv(1024)
    print data



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
        #this func lists csurrent sessions in the server
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

s.close