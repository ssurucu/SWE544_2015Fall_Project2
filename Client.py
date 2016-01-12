import sys
import socket
import threading
import Queue
from PyQt4 import QtCore, QtGui
from tombalaGameUI import Ui_MainWindow
import time

screenQueue = Queue.Queue()
selectedNumber = "-"
ticketArray = []
threadQueue = Queue.Queue()
onlineMemberQueue = Queue.Queue()
s = socket.socket()
host = socket.gethostname()
port = 5000
username=""


class ClientDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.CinkoPress)

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
        #self.timer2.timeout.connect(self.memberListRefresh)
        #self.timer2.start(1500)

        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.updateSelectedNumber)
        self.timer3.start(10)


        readerThread = ReadQThread()
        readerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(readerThread)
        readerThread.start()

        writerThread = WriteQThread()
        writerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(writerThread)
        writerThread.start()

        #threadQueue._put("LOG "+username)

    def CinkoPress(self):
        threadQueue._put("CIN")

    def fillTicket(self):
        self.ui.label_0_0.setText(str(ticketArray[0][0]))
        self.ui.label_0_1.setText(str(ticketArray[0][1]))
        self.ui.label_0_2.setText(str(ticketArray[0][2]))
        self.ui.label_0_3.setText(str(ticketArray[0][3]))
        self.ui.label_0_4.setText(str(ticketArray[0][4]))
        self.ui.label_1_0.setText(str(ticketArray[1][0]))
        self.ui.label_1_1.setText(str(ticketArray[1][1]))
        self.ui.label_1_2.setText(str(ticketArray[1][2]))
        self.ui.label_1_3.setText(str(ticketArray[1][3]))
        self.ui.label_1_4.setText(str(ticketArray[1][4]))
        self.ui.label_2_0.setText(str(ticketArray[2][0]))
        self.ui.label_2_1.setText(str(ticketArray[2][1]))
        self.ui.label_2_2.setText(str(ticketArray[2][2]))
        self.ui.label_2_3.setText(str(ticketArray[2][3]))
        self.ui.label_2_4.setText(str(ticketArray[2][4]))



    # this function parses the message texts into the format of protocol
    def outgoing_parser(self, data):
        threadQueue.put(str("QUI"))

    # this function gets item(s) from screenqueue (if any exits) and adds to messageScreen
    def updateChannelWindow(self):
        if screenQueue.qsize() > 0:
            queue_message = screenQueue.get()
            self.ui.listWidget.addItem(unicode(queue_message))
            self.ui.listWidget.scrollToBottom()

    def updateSelectedNumber(self):
        self.ui.label_2.setText(selectedNumber)

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
        self.ui.listWidget.addItem('Just wait until 3 people are joined the game')
        self.ui.listWidget.addItem('---------------------------------------------------')

class ReadQThread(QtCore.QThread):
    data_read = QtCore.pyqtSignal(object)
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        time.sleep(2)
        while True:
            data = s.recv(1024)
            print data
            self.incoming_parser(data)

    def incoming_parser(self, data):
        #print data
        #screenQueue._put(data)
        global selectedNumber
        global assignedTicket

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
            screenQueue._put(str(data[4:]))
        if data[0:3] == "ATI":
            #User is getting the ticket
            assignedTicket = data[4:]
            self.fillTheTicket()
        if data[0:3] == "PNA":
            selectedNumber = str(data[4:])
            #screenQueue._put(selectedNumber)
            print data[4:]
            #Randomly picked number announce
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

    def fillTheTicket(self):
        #this func lists csurrent sessions in the server
        global ticketArray
        ticket= []
        print assignedTicket
        ticketRows = assignedTicket.split(";")
        ticketRow0 = ticketRows[0].split(",")
        ticketRow1 = ticketRows[1].split(",")
        ticketRow2 = ticketRows[2].split(",")

        ticket.append(ticketRow0)
        ticket.append(ticketRow1)
        ticket.append(ticketRow2)

        ticketArray = ticket
        myapp.fillTicket()


class WriteQThread(QtCore.QThread):
    data_read = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            if threadQueue.qsize() > 0:
                print "sdasd"
                queue_message = threadQueue.get()
                try:
                    s.send(queue_message)
                except socket.error:
                    s.close()
                    break


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #username = raw_input("Please enter username: ")
    username = "sinan"
    myapp = ClientDialog()
    # myapp.show()
    sys.exit(app.exec_())
