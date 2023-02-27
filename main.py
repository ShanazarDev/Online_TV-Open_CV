from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QSizePolicy, QGridLayout
from PyQt5.QtCore import QTimer, Qt
import sys, cv2, os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        icon = QIcon()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'img/live.png')
        icon.addPixmap(QPixmap(filename), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: hsl(220, 60%, 70%)")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 440, 85, 30))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 35, 250, 35))
        font = QtGui.QFont();font.setFamily("Times New Roman");font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel""{""Color: white;""}")
        self.label.setObjectName("label")

        self.lblVid = QLabel(self.centralwidget)
        self.gridLayout = QGridLayout(self.lblVid)
        self.lblVid.setGeometry(QtCore.QRect(20, 90, 501, 350))
        self.lblVid = QLabel(self.centralwidget)
        self.lblVid.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.gridLayout.addWidget(self.lblVid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #btn
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : red;""}")

        #altyn asyr
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(540, 55, 190, 30))
        self.btn1.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn1.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn1.setFont(font)
        filename = os.path.join(dirname, 'img/altyn_asyr.png')
        icon = QIcon(filename)
        self.btn1.setIcon(icon)
        self.btn1.setIconSize(QtCore.QSize(70, 70))
        self.btn1.setObjectName("pushButton")
        
        #yaslyk
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(540, 100, 190, 30))
        self.btn2.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("QPushButton""{""Color: white;""}")
        filename = os.path.join(dirname, 'img/yaslyk.png')
        icon = QIcon(filename)
        self.btn2.setIcon(icon)
        self.btn2.setIconSize(QtCore.QSize(70, 70))
        self.btn2.setObjectName("pushButton")
        
        #miras
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(540, 150, 190, 30))
        self.btn3.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn3.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn3.setFont(font)
        filename = os.path.join(dirname, 'img/miras.png')
        icon = QIcon(filename)
        self.btn3.setIcon(icon)
        self.btn3.setIconSize(QtCore.QSize(40, 70))
        self.btn3.setObjectName("pushButton")
        
        #tkm
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(540, 200, 190, 30))
        self.btn4.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn4.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn4.setFont(font)
        filename = os.path.join(dirname, 'img/tkm.png')
        icon = QIcon(filename)
        self.btn4.setIcon(icon)
        self.btn4.setIconSize(QtCore.QSize(70, 70))
        self.btn4.setObjectName("pushButton")
        
        #owaz
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(540, 250, 190, 30))
        self.btn5.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn5.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn5.setFont(font)
        filename = os.path.join(dirname, 'img/owaz.png')
        icon = QIcon(filename)
        self.btn5.setIcon(icon)
        self.btn5.setIconSize(QtCore.QSize(30, 70))
        self.btn5.setObjectName("pushButton")
        
        #asg
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(540, 300, 190, 30))
        self.btn6.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn6.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn6.setFont(font)
        filename = os.path.join(dirname, 'img/asg.png')
        icon = QIcon(filename)
        self.btn6.setIcon(icon)
        self.btn6.setIconSize(QtCore.QSize(40, 70))
        self.btn6.setObjectName("pushButton")
        
        #sport
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(540, 350, 190, 30))
        self.btn7.setStyleSheet("QPushButton""{""background-color : hsl(194,29%,67%);""}""QPushButton::pressed""{""background-color : lightblue;""}")
        self.btn7.setStyleSheet("QPushButton""{""Color: white;""}")
        self.btn7.setFont(font)
        filename = os.path.join(dirname, 'img/sport.png')
        icon = QIcon(filename)
        self.btn7.setIcon(icon)
        self.btn7.setIconSize(QtCore.QSize(30, 70))
        self.btn7.setObjectName("pushButton")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Kanalar
        self.altyn_asyr = "https://alpha.tv.online.tm/hls/ch001.m3u8"
        self.yaslyk = 'https://alpha.tv.online.tm/hls/ch002.m3u8'
        self.miras = 'https://alpha.tv.online.tm/hls/ch003.m3u8'
        self.tkm = 'https://alpha.tv.online.tm/hls/ch007.m3u8'
        self.tkm_owaz = 'https://alpha.tv.online.tm/hls/ch005.m3u8'
        self.asg = 'https://alpha.tv.online.tm/hls/ch006.m3u8'
        self.tkm_sport = 'https://alpha.tv.online.tm/hls/ch004.m3u8'
       
        # Если алфа канал закрыт или не отвечает можно исползовать эти ссылки место альфа!
        # self.Horjun_A_A = "https://horjuntv.com.tm/chanel2/ch001_400/index.m3u8"
        # self.Horjun_Y = "https://horjuntv.com.tm/chanel2/ch002_400/index.m3u8"
        # self.Horjun_M = "https://horjuntv.com.tm/chanel2/ch003_400/index.m3u8"
        # self.Horjun_TKM = "https://horjuntv.com.tm/chanel2/ch004_400/index.m3u8"
        # self.Horjun_O = "https://horjuntv.com.tm/chanel2/ch005_400/index.m3u8"
        # self.Horjun_A = "https://horjuntv.com.tm/chanel2/ch006_400/index.m3u8"
        # self.Horjun_S = "https://horjuntv.com.tm/chanel2/ch007_400/index.m3u8"


        self.btn1.clicked.connect(self.ch_1)
        self.btn2.clicked.connect(self.ch_2)
        self.btn3.clicked.connect(self.ch_3)
        self.btn4.clicked.connect(self.ch_4)
        self.btn5.clicked.connect(self.ch_5)
        self.btn6.clicked.connect(self.ch_6)
        self.btn7.clicked.connect(self.ch_7)

        #yapmak
        self.pushButton.pressed.connect(self.close)
    
    #btn func
    def ch_1(self):
        self.startVideo(self.altyn_asyr)
        self.label.setText("Altyn Asyr")
    def ch_2(self):
        self.startVideo(self.yaslyk)
        self.label.setText("Ýaşlyk")
    def ch_3(self):
        self.startVideo(self.miras)
        self.label.setText("Miras")
    def ch_4(self):
        self.startVideo(self.tkm)
        self.label.setText("Türkmenistan")
    def ch_5(self):
        self.startVideo(self.tkm_owaz)
        self.label.setGeometry(QtCore.QRect(250, 35, 250, 35))
        self.label.setText("Türkmen Owazy")
    def ch_6(self):
        self.startVideo(self.asg)
        self.label.setText("Aşgabat")
    def ch_7(self):
        self.startVideo(self.tkm_sport)
        self.label.setGeometry(QtCore.QRect(250, 35, 250, 35))
        self.label.setText("Türkmen Sport")

  
    # close func
    def close(self):
        sys.exit()

    #live stream
    def startVideo(self, link):
        self.cap = cv2.VideoCapture(link)
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.timer = QTimer()
        millisecs = int(1000.0 / fps)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(millisecs)
  
    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame,frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)            
            pix = pix.scaled(self.lblVid.width(), self.lblVid.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.lblVid.setPixmap(pix)    
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Göni ýaýlym"))
        self.pushButton.setText(_translate("MainWindow", "Çykmak"))
        self.btn1.setText(_translate("MainWindow", "Altyn Asyr"))
        self.btn2.setText(_translate("MainWindow", "Ýaşlyk"))
        self.btn3.setText(_translate("MainWindow", "Miras"))
        self.btn4.setText(_translate("MainWindow", "Türkmenistan"))
        self.btn5.setText(_translate("MainWindow", "Türkmen Owazy"))
        self.btn6.setText(_translate("MainWindow", "Aşgabat"))
        self.btn7.setText(_translate("MainWindow", "Türkmen Sport"))
        self.label.setText("Online TV ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())