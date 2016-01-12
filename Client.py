import sys
import socket
import threading
import Queue
from PyQt4 import QtCore, QtGui
from tombalaGameUI import Ui_MainWindow
import time

screenQueue = Queue.Queue()
threadQueue = Queue.Queue()
onlineMemberQueue = Queue.Queue()
s = socket.socket()
host = socket.gethostname()
port = 12345
username=""


class ClientDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print threading.current_thread()
        self.show()
        self.connectToGameServer();

        self.threads = []

        # timer has been set for updating channel window every 10ms
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateChannelWindow)
        self.timer.start(10)

        # timer has been set for updating member list every 1.5s
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.memberListRefresh)
        #self.timer2.start(1500)

        readerThread = ReadQThread()
        readerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(readerThread)
        readerThread.start()

        writerThread = WriteQThread()
        writerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(writerThread)
        writerThread.start()

        threadQueue._put("LOG "+username)

    # this function parses the message texts into the format of protocol
    def outgoing_parser(self, data):
        threadQueue.put(str("QUI"))

    # this function gets item(s) from screenqueue (if any exits) and adds to messageScreen
    def updateChannelWindow(self):
        if screenQueue.qsize() > 0:
            queue_message = screenQueue.get()
            self.ui.listWidget.addItem(unicode(queue_message))
            self.ui.listWidget.scrollToBottom()


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

    def connectToGameServer(self):
        self.ui.listWidget.addItem('Please be patient while your connection is established with the server...')
        s.connect((host, int(port)))

        self.ui.listWidget.addItem('Now you are connected to the server! Wait for the game to start')
        self.ui.listWidget.addItem('---------------------------------------------------')

class ReadQThread(QtCore.QThread):
    data_read = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            data = s.recv(1024)
            self.incoming_parser(data)

    def incoming_parser(self, data):
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


class WriteQThread(QtCore.QThread):
    data_read = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            if threadQueue.qsize() > 0:
                queue_message = threadQueue.get()
                try:
                    s.send(queue_message)
                except socket.error:
                    s.close()
                    break


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    username = raw_input("Please enter username: ")
    myapp = ClientDialog()
    # myapp.show()
    sys.exit(app.exec_())
