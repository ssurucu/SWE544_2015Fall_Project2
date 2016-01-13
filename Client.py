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
ticketArray = []

threadQueue = Queue.Queue()
onlineMemberQueue = Queue.Queue()
s = socket.socket()
host = socket.gethostname()
port = 5000
username=""
isGameFinished = False


class ClientDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.requestCinko)
        self.ui.label_0_0.clicked.connect(self.selectTheNumber_00)
        self.ui.label_0_1.clicked.connect(self.selectTheNumber_01)
        self.ui.label_0_2.clicked.connect(self.selectTheNumber_02)
        self.ui.label_0_3.clicked.connect(self.selectTheNumber_03)
        self.ui.label_0_4.clicked.connect(self.selectTheNumber_04)
        self.ui.label_1_0.clicked.connect(self.selectTheNumber_10)
        self.ui.label_1_1.clicked.connect(self.selectTheNumber_11)
        self.ui.label_1_2.clicked.connect(self.selectTheNumber_12)
        self.ui.label_1_3.clicked.connect(self.selectTheNumber_13)
        self.ui.label_1_4.clicked.connect(self.selectTheNumber_14)
        self.ui.label_2_0.clicked.connect(self.selectTheNumber_20)
        self.ui.label_2_1.clicked.connect(self.selectTheNumber_21)
        self.ui.label_2_2.clicked.connect(self.selectTheNumber_22)
        self.ui.label_2_3.clicked.connect(self.selectTheNumber_23)
        self.ui.label_2_4.clicked.connect(self.selectTheNumber_24)

        print threading.current_thread()
        self.show()
        self.connectToGameServer();

        self.threads = []

        # timer has been set for updating channel window every 10ms
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateChannelWindow)
        self.timer.start(10)

        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.updateSelectedNumber)
        self.timer3.start(10)

        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.learnCinkoStatus)
        self.timer4.start(1000)

        readerThread = ReadQThread()
        readerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(readerThread)
        readerThread.start()

        writerThread = WriteQThread()
        writerThread.data_read.connect(self.updateChannelWindow)
        self.threads.append(writerThread)
        writerThread.start()

        self.loginToServer(username)


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

    def selectTheNumber_00(self):
        #sending_button = self.sender()
        #print sending_button.objectName()
        self.ui.label_0_0.setStyleSheet("background-color: orange")

    def selectTheNumber_01(self):
        self.ui.label_0_1.setStyleSheet("background-color: orange")

    def selectTheNumber_02(self):
        self.ui.label_0_2.setStyleSheet("background-color: orange")

    def selectTheNumber_03(self):
        self.ui.label_0_3.setStyleSheet("background-color: orange")

    def selectTheNumber_04(self):
        self.ui.label_0_4.setStyleSheet("background-color: orange")

    def selectTheNumber_05(self):
        self.ui.label_0_5.setStyleSheet("background-color: orange")

    def selectTheNumber_10(self):
        self.ui.label_1_0.setStyleSheet("background-color: orange")

    def selectTheNumber_11(self):
        self.ui.label_1_1.setStyleSheet("background-color: orange")

    def selectTheNumber_12(self):
        self.ui.label_1_2.setStyleSheet("background-color: orange")

    def selectTheNumber_13(self):
        self.ui.label_1_3.setStyleSheet("background-color: orange")

    def selectTheNumber_14(self):
        self.ui.label_1_4.setStyleSheet("background-color: orange")

    def selectTheNumber_20(self):
        self.ui.label_2_0.setStyleSheet("background-color: orange")

    def selectTheNumber_21(self):
        self.ui.label_2_1.setStyleSheet("background-color: orange")

    def selectTheNumber_22(self):
        self.ui.label_2_2.setStyleSheet("background-color: orange")

    def selectTheNumber_23(self):
        self.ui.label_2_3.setStyleSheet("background-color: orange")

    def selectTheNumber_24(self):
        self.ui.label_2_4.setStyleSheet("background-color: orange")

    def signTheNumber(self, number):
        if not isGameFinished:
            if(str(number)=="1"):
                self.ui.label_01.setStyleSheet("background-color: red")
            if(str(number)=="2"):
                self.ui.label_02.setStyleSheet("background-color: red")
            if(str(number)=="3"):
                self.ui.label_03.setStyleSheet("background-color: red")
            if(str(number)=="4"):
                self.ui.label_04.setStyleSheet("background-color: red")
            if(str(number)=="5"):
                self.ui.label_05.setStyleSheet("background-color: red")
            if(str(number)=="6"):
                self.ui.label_06.setStyleSheet("background-color: red")
            if(str(number)=="7"):
                self.ui.label_07.setStyleSheet("background-color: red")
            if(str(number)=="8"):
                self.ui.label_08.setStyleSheet("background-color: red")
            if(str(number)=="9"):
                self.ui.label_09.setStyleSheet("background-color: red")
            if(str(number)=="10"):
                self.ui.label_10.setStyleSheet("background-color: red")
            if(str(number)=="11"):
                self.ui.label_11.setStyleSheet("background-color: red")
            if(str(number)=="12"):
                self.ui.label_12.setStyleSheet("background-color: red")
            if(str(number)=="13"):
                self.ui.label_13.setStyleSheet("background-color: red")
            if(str(number)=="14"):
                self.ui.label_14.setStyleSheet("background-color: red")
            if(str(number)=="15"):
                self.ui.label_15.setStyleSheet("background-color: red")
            if(str(number)=="16"):
                self.ui.label_16.setStyleSheet("background-color: red")
            if(str(number)=="17"):
                self.ui.label_17.setStyleSheet("background-color: red")
            if(str(number)=="18"):
                self.ui.label_18.setStyleSheet("background-color: red")
            if(str(number)=="19"):
                self.ui.label_19.setStyleSheet("background-color: red")
            if(str(number)=="20"):
                self.ui.label_20.setStyleSheet("background-color: red")
            if(str(number)=="21"):
                self.ui.label_21.setStyleSheet("background-color: red")
            if(str(number)=="22"):
                self.ui.label_22.setStyleSheet("background-color: red")
            if(str(number)=="23"):
                self.ui.label_23.setStyleSheet("background-color: red")
            if(str(number)=="24"):
                self.ui.label_24.setStyleSheet("background-color: red")
            if(str(number)=="25"):
                self.ui.label_25.setStyleSheet("background-color: red")
            if(str(number)=="26"):
                self.ui.label_26.setStyleSheet("background-color: red")
            if(str(number)=="27"):
                self.ui.label_27.setStyleSheet("background-color: red")
            if(str(number)=="28"):
                self.ui.label_28.setStyleSheet("background-color: red")
            if(str(number)=="29"):
                self.ui.label_29.setStyleSheet("background-color: red")
            if(str(number)=="30"):
                self.ui.label_30.setStyleSheet("background-color: red")
            if(str(number)=="31"):
                self.ui.label_31.setStyleSheet("background-color: red")
            if(str(number)=="32"):
                self.ui.label_32.setStyleSheet("background-color: red")
            if(str(number)=="33"):
                self.ui.label_33.setStyleSheet("background-color: red")
            if(str(number)=="34"):
                self.ui.label_34.setStyleSheet("background-color: red")
            if(str(number)=="35"):
                self.ui.label_35.setStyleSheet("background-color: red")
            if(str(number)=="36"):
                self.ui.label_36.setStyleSheet("background-color: red")
            if(str(number)=="37"):
                self.ui.label_37.setStyleSheet("background-color: red")
            if(str(number)=="38"):
                self.ui.label_38.setStyleSheet("background-color: red")
            if(str(number)=="39"):
                self.ui.label_39.setStyleSheet("background-color: red")
            if(str(number)=="40"):
                self.ui.label_40.setStyleSheet("background-color: red")
            if(str(number)=="41"):
                self.ui.label_41.setStyleSheet("background-color: red")
            if(str(number)=="42"):
                self.ui.label_42.setStyleSheet("background-color: red")
            if(str(number)=="43"):
                self.ui.label_43.setStyleSheet("background-color: red")
            if(str(number)=="44"):
                self.ui.label_44.setStyleSheet("background-color: red")
            if(str(number)=="45"):
                self.ui.label_45.setStyleSheet("background-color: red")
            if(str(number)=="46"):
                self.ui.label_46.setStyleSheet("background-color: red")
            if(str(number)=="47"):
                self.ui.label_47.setStyleSheet("background-color: red")
            if(str(number)=="48"):
                self.ui.label_48.setStyleSheet("background-color: red")
            if(str(number)=="49"):
                self.ui.label_49.setStyleSheet("background-color: red")
            if(str(number)=="50"):
                self.ui.label_50.setStyleSheet("background-color: red")
            if(str(number)=="51"):
                self.ui.label_51.setStyleSheet("background-color: red")
            if(str(number)=="52"):
                self.ui.label_52.setStyleSheet("background-color: red")
            if(str(number)=="53"):
                self.ui.label_53.setStyleSheet("background-color: red")
            if(str(number)=="54"):
                self.ui.label_54.setStyleSheet("background-color: red")
            if(str(number)=="55"):
                self.ui.label_55.setStyleSheet("background-color: red")
            if(str(number)=="56"):
                self.ui.label_56.setStyleSheet("background-color: red")
            if(str(number)=="57"):
                self.ui.label_57.setStyleSheet("background-color: red")
            if(str(number)=="58"):
                self.ui.label_58.setStyleSheet("background-color: red")
            if(str(number)=="59"):
                self.ui.label_59.setStyleSheet("background-color: red")
            if(str(number)=="60"):
                self.ui.label_60.setStyleSheet("background-color: red")
            if(str(number)=="61"):
                self.ui.label_61.setStyleSheet("background-color: red")
            if(str(number)=="62"):
                self.ui.label_62.setStyleSheet("background-color: red")
            if(str(number)=="63"):
                self.ui.label_63.setStyleSheet("background-color: red")
            if(str(number)=="64"):
                self.ui.label_64.setStyleSheet("background-color: red")
            if(str(number)=="65"):
                self.ui.label_65.setStyleSheet("background-color: red")
            if(str(number)=="66"):
                self.ui.label_66.setStyleSheet("background-color: red")
            if(str(number)=="67"):
                self.ui.label_67.setStyleSheet("background-color: red")
            if(str(number)=="68"):
                self.ui.label_68.setStyleSheet("background-color: red")
            if(str(number)=="69"):
                self.ui.label_69.setStyleSheet("background-color: red")
            if(str(number)=="70"):
                self.ui.label_70.setStyleSheet("background-color: red")
            if(str(number)=="71"):
                self.ui.label_71.setStyleSheet("background-color: red")
            if(str(number)=="72"):
                self.ui.label_72.setStyleSheet("background-color: red")
            if(str(number)=="73"):
                self.ui.label_73.setStyleSheet("background-color: red")
            if(str(number)=="74"):
                self.ui.label_74.setStyleSheet("background-color: red")
            if(str(number)=="75"):
                self.ui.label_75.setStyleSheet("background-color: red")
            if(str(number)=="76"):
                self.ui.label_76.setStyleSheet("background-color: red")
            if(str(number)=="77"):
                self.ui.label_77.setStyleSheet("background-color: red")
            if(str(number)=="78"):
                self.ui.label_78.setStyleSheet("background-color: red")
            if(str(number)=="79"):
                self.ui.label_79.setStyleSheet("background-color: red")
            if(str(number)=="80"):
                self.ui.label_80.setStyleSheet("background-color: red")
            if(str(number)=="81"):
                self.ui.label_81.setStyleSheet("background-color: red")
            if(str(number)=="82"):
                self.ui.label_82.setStyleSheet("background-color: red")
            if(str(number)=="83"):
                self.ui.label_83.setStyleSheet("background-color: red")
            if(str(number)=="84"):
                self.ui.label_84.setStyleSheet("background-color: red")
            if(str(number)=="85"):
                self.ui.label_85.setStyleSheet("background-color: red")
            if(str(number)=="86"):
                self.ui.label_86.setStyleSheet("background-color: red")
            if(str(number)=="87"):
                self.ui.label_87.setStyleSheet("background-color: red")
            if(str(number)=="88"):
                self.ui.label_88.setStyleSheet("background-color: red")
            if(str(number)=="89"):
                self.ui.label_89.setStyleSheet("background-color: red")
            if(str(number)=="90"):
                self.ui.label_90.setStyleSheet("background-color: red")
            if(str(number)=="91"):
                self.ui.label_91.setStyleSheet("background-color: red")
            if(str(number)=="92"):
                self.ui.label_92.setStyleSheet("background-color: red")
            if(str(number)=="93"):
                self.ui.label_93.setStyleSheet("background-color: red")
            if(str(number)=="94"):
                self.ui.label_94.setStyleSheet("background-color: red")
            if(str(number)=="95"):
                self.ui.label_95.setStyleSheet("background-color: red")
            if(str(number)=="96"):
                self.ui.label_96.setStyleSheet("background-color: red")
            if(str(number)=="97"):
                self.ui.label_97.setStyleSheet("background-color: red")
            if(str(number)=="98"):
                self.ui.label_98.setStyleSheet("background-color: red")
            if(str(number)=="99"):
                self.ui.label_99.setStyleSheet("background-color: red")




    def learnCinko(self, data):
        self.timer3.start()

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
        if not isGameFinished:
            self.ui.label_2.setText(selectedNumber)

    #Initial functions
    def loginToServer(self,username):
        #this func porvides login to server
        threadQueue._put("LOG "+username)
        print "server accepted login"

    def setCinkoStatusses(self, data):
        #this func provides to set cinko statusess
        data = data[:-1]
        data = data[1:]
        dataArray = data.split(",")

        self.ui.label_p1.setText("Cinko Count:" + str(dataArray[0]))
        self.ui.label_p2.setText("Cinko Count:" + str(dataArray[1]))
        self.ui.label_p3.setText("Cinko Count:" + str(dataArray[2]))
        self.ui.label_p4.setText("Cinko Count:" + str(dataArray[3]))


    def getUserNames(self, data):
        #this func provides to set cinko statusess
        data = data[:-1]
        data = data[1:]
        dataArray = data.split(",")

        self.ui.label_p1_name.setText(str(dataArray[0]))
        self.ui.label_p2_name.setText(str(dataArray[1]))
        self.ui.label_p3_name.setText(str(dataArray[2]))
        self.ui.label_p4_name.setText(str(dataArray[3]))


    def requestCinko(self):
        #this func will be used for requestin a cinko
        threadQueue._put("CIN")

    def learnCinkoStatus(self):
        #this func will be used for selecting a number
        threadQueue._put("LBS")

    def connectToGameServer(self):
        self.ui.listWidget.addItem('Please be patient while your connection is established with the server...')
        s.connect((host, int(port)))

        self.ui.listWidget.addItem('Now you are connected to the server! Wait for the game to start')
        self.ui.listWidget.addItem('Just wait until 4 people are joined the game')
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
        global selectedNumber
        global assignedTicket
        global isGameFinished

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
            myapp.getUserNames(data[4:])
            screenQueue._put("Game will start in 3 seconds")
        if data[0:3] == "ATI":
            #User is getting the ticket
            assignedTicket = data[4:]
            self.fillTheTicket()
        if data[0:3] == "PNA":
            selectedNumber = str(data[4:])
            myapp.signTheNumber(selectedNumber)
            #screenQueue._put(selectedNumber)
            print data[4:]
            #Randomly picked number announce
        if data[0:3] == "NSA":
            #User selects number
            print 'data'
        if data[0:3] == "CRA":
            #Cinko requested, cinko is valid
            screenQueue._put(data)
            print 'data'
        if data[0:3] == "CRR":
            #Cinko requested, cinko is invalid
            screenQueue._put("Your cinko is invalid")
            screenQueue._put("Careful! After 3 invalid Cinkos, you will be banned!")
            print 'data'
        if data[0:3] == "CRB":
            #Too many invalid Cinko request, user banned for the session
            screenQueue._put("Too many invalid cinkos. You are banned for this session")
            print 'data'
        if data[0:3] == "LBA":
            #Learn Cinko status of a user
            myapp.setCinkoStatusses(data[4:])
        if data[0:3] == "GFA":
            #Game finished, winner username is returned
            isGameFinished = True
            screenQueue._put("The Game has been finished! Congs to " + str(data[4:]))
        if data[0:3] == "ACI":
            #A user (username) has made a cinko
            screenQueue._put("A user has made a Cinko! Congs")
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
    username = raw_input("Please enter username: ")
    #username = "sinan"
    myapp = ClientDialog()
    # myapp.show()
    sys.exit(app.exec_())
