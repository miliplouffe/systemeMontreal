# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 571)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Label1 = QLabel(self.centralwidget)
        self.Label1.setObjectName(u"Label1")
        self.Label1.setGeometry(QRect(30, 230, 151, 31))
        font = QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.Label1.setFont(font)
        self.Label1.setFrameShape(QFrame.NoFrame)
        self.Label2 = QLabel(self.centralwidget)
        self.Label2.setObjectName(u"Label2")
        self.Label2.setGeometry(QRect(30, 270, 161, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.Label2.setFont(font1)
        self.Label4 = QLabel(self.centralwidget)
        self.Label4.setObjectName(u"Label4")
        self.Label4.setGeometry(QRect(30, 150, 161, 31))
        self.Label4.setFont(font1)
        self.Label3 = QLabel(self.centralwidget)
        self.Label3.setObjectName(u"Label3")
        self.Label3.setGeometry(QRect(30, 110, 141, 31))
        self.Label3.setFont(font1)
        self.ChambrePrincipaleCercle = QLabel(self.centralwidget)
        self.ChambrePrincipaleCercle.setObjectName(u"ChambrePrincipaleCercle")
        self.ChambrePrincipaleCercle.setGeometry(QRect(220, 230, 31, 31))
        self.ChambrePrincipaleCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.ChambreSecondaireCercle = QLabel(self.centralwidget)
        self.ChambreSecondaireCercle.setObjectName(u"ChambreSecondaireCercle")
        self.ChambreSecondaireCercle.setGeometry(QRect(220, 270, 31, 31))
        self.ChambreSecondaireCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.PorteAvantCercle = QLabel(self.centralwidget)
        self.PorteAvantCercle.setObjectName(u"PorteAvantCercle")
        self.PorteAvantCercle.setGeometry(QRect(220, 110, 31, 31))
        self.PorteAvantCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.PorteArriereCercle = QLabel(self.centralwidget)
        self.PorteArriereCercle.setObjectName(u"PorteArriereCercle")
        self.PorteArriereCercle.setGeometry(QRect(220, 150, 31, 31))
        self.PorteArriereCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 331, 31))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.Label4_2 = QLabel(self.centralwidget)
        self.Label4_2.setObjectName(u"Label4_2")
        self.Label4_2.setGeometry(QRect(30, 190, 161, 31))
        self.Label4_2.setFont(font1)
        self.PorteSousSolCercle = QLabel(self.centralwidget)
        self.PorteSousSolCercle.setObjectName(u"PorteSousSolCercle")
        self.PorteSousSolCercle.setGeometry(QRect(220, 190, 31, 31))
        self.PorteSousSolCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label2_2 = QLabel(self.centralwidget)
        self.Label2_2.setObjectName(u"Label2_2")
        self.Label2_2.setGeometry(QRect(30, 310, 161, 31))
        self.Label2_2.setFont(font1)
        self.BureauCercle = QLabel(self.centralwidget)
        self.BureauCercle.setObjectName(u"BureauCercle")
        self.BureauCercle.setGeometry(QRect(220, 310, 31, 31))
        self.BureauCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label2_3 = QLabel(self.centralwidget)
        self.Label2_3.setObjectName(u"Label2_3")
        self.Label2_3.setGeometry(QRect(30, 350, 161, 31))
        self.Label2_3.setFont(font1)
        self.SalonCercle = QLabel(self.centralwidget)
        self.SalonCercle.setObjectName(u"SalonCercle")
        self.SalonCercle.setGeometry(QRect(220, 350, 31, 31))
        self.SalonCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.SalleBillardCercle = QLabel(self.centralwidget)
        self.SalleBillardCercle.setObjectName(u"SalleBillardCercle")
        self.SalleBillardCercle.setGeometry(QRect(480, 110, 31, 31))
        self.SalleBillardCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_3 = QLabel(self.centralwidget)
        self.Label4_3.setObjectName(u"Label4_3")
        self.Label4_3.setGeometry(QRect(290, 110, 161, 31))
        self.Label4_3.setFont(font1)
        self.SalleVernisCercle = QLabel(self.centralwidget)
        self.SalleVernisCercle.setObjectName(u"SalleVernisCercle")
        self.SalleVernisCercle.setGeometry(QRect(480, 150, 31, 31))
        self.SalleVernisCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_4 = QLabel(self.centralwidget)
        self.Label4_4.setObjectName(u"Label4_4")
        self.Label4_4.setGeometry(QRect(290, 150, 161, 31))
        self.Label4_4.setFont(font1)
        self.ReservoirEauChaudeCercle = QLabel(self.centralwidget)
        self.ReservoirEauChaudeCercle.setObjectName(u"ReservoirEauChaudeCercle")
        self.ReservoirEauChaudeCercle.setGeometry(QRect(480, 190, 31, 31))
        self.ReservoirEauChaudeCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.FumeeSalleBillardCercle = QLabel(self.centralwidget)
        self.FumeeSalleBillardCercle.setObjectName(u"FumeeSalleBillardCercle")
        self.FumeeSalleBillardCercle.setGeometry(QRect(480, 270, 31, 31))
        self.FumeeSalleBillardCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_5 = QLabel(self.centralwidget)
        self.Label4_5.setObjectName(u"Label4_5")
        self.Label4_5.setGeometry(QRect(290, 270, 161, 31))
        self.Label4_5.setFont(font1)
        self.EntreeEauCercle = QLabel(self.centralwidget)
        self.EntreeEauCercle.setObjectName(u"EntreeEauCercle")
        self.EntreeEauCercle.setGeometry(QRect(480, 230, 31, 31))
        self.EntreeEauCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_6 = QLabel(self.centralwidget)
        self.Label4_6.setObjectName(u"Label4_6")
        self.Label4_6.setGeometry(QRect(290, 190, 161, 31))
        self.Label4_6.setFont(font1)
        self.Label4_7 = QLabel(self.centralwidget)
        self.Label4_7.setObjectName(u"Label4_7")
        self.Label4_7.setGeometry(QRect(290, 230, 161, 31))
        self.Label4_7.setFont(font1)
        self.Label4_8 = QLabel(self.centralwidget)
        self.Label4_8.setObjectName(u"Label4_8")
        self.Label4_8.setGeometry(QRect(290, 310, 161, 31))
        self.Label4_8.setFont(font1)
        self.FumeeAtelierCercle = QLabel(self.centralwidget)
        self.FumeeAtelierCercle.setObjectName(u"FumeeAtelierCercle")
        self.FumeeAtelierCercle.setGeometry(QRect(480, 310, 31, 31))
        self.FumeeAtelierCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.SystemeArmeCercle = QLabel(self.centralwidget)
        self.SystemeArmeCercle.setObjectName(u"SystemeArmeCercle")
        self.SystemeArmeCercle.setGeometry(QRect(680, 20, 211, 31))
        self.SystemeArmeCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_9 = QLabel(self.centralwidget)
        self.Label4_9.setObjectName(u"Label4_9")
        self.Label4_9.setGeometry(QRect(560, 20, 111, 31))
        self.Label4_9.setFont(font1)
        self.Bouton1 = QPushButton(self.centralwidget)
        self.Bouton1.setObjectName(u"Bouton1")
        self.Bouton1.setGeometry(QRect(560, 120, 131, 91))
        font3 = QFont()
        font3.setPointSize(60)
        self.Bouton1.setFont(font3)
        self.Bouton2 = QPushButton(self.centralwidget)
        self.Bouton2.setObjectName(u"Bouton2")
        self.Bouton2.setGeometry(QRect(720, 120, 131, 91))
        self.Bouton2.setFont(font3)
        self.Bouton3 = QPushButton(self.centralwidget)
        self.Bouton3.setObjectName(u"Bouton3")
        self.Bouton3.setGeometry(QRect(870, 120, 131, 91))
        self.Bouton3.setFont(font3)
        self.Bouton5 = QPushButton(self.centralwidget)
        self.Bouton5.setObjectName(u"Bouton5")
        self.Bouton5.setGeometry(QRect(720, 220, 131, 91))
        self.Bouton5.setFont(font3)
        self.Bouton4 = QPushButton(self.centralwidget)
        self.Bouton4.setObjectName(u"Bouton4")
        self.Bouton4.setGeometry(QRect(560, 220, 131, 91))
        self.Bouton4.setFont(font3)
        self.Bouton6 = QPushButton(self.centralwidget)
        self.Bouton6.setObjectName(u"Bouton6")
        self.Bouton6.setGeometry(QRect(870, 220, 131, 91))
        self.Bouton6.setFont(font3)
        self.Bouton8 = QPushButton(self.centralwidget)
        self.Bouton8.setObjectName(u"Bouton8")
        self.Bouton8.setGeometry(QRect(720, 320, 131, 91))
        self.Bouton8.setFont(font3)
        self.Bouton7 = QPushButton(self.centralwidget)
        self.Bouton7.setObjectName(u"Bouton7")
        self.Bouton7.setGeometry(QRect(560, 320, 131, 91))
        self.Bouton7.setFont(font3)
        self.Bouton9 = QPushButton(self.centralwidget)
        self.Bouton9.setObjectName(u"Bouton9")
        self.Bouton9.setGeometry(QRect(870, 320, 131, 91))
        self.Bouton9.setFont(font3)
        self.Bouton0 = QPushButton(self.centralwidget)
        self.Bouton0.setObjectName(u"Bouton0")
        self.Bouton0.setGeometry(QRect(720, 420, 131, 91))
        self.Bouton0.setFont(font3)
        self.BoutonStar = QPushButton(self.centralwidget)
        self.BoutonStar.setObjectName(u"BoutonStar")
        self.BoutonStar.setGeometry(QRect(560, 420, 131, 91))
        self.BoutonStar.setFont(font3)
        self.BoutonReset = QPushButton(self.centralwidget)
        self.BoutonReset.setObjectName(u"BoutonReset")
        self.BoutonReset.setGeometry(QRect(870, 420, 131, 92))
        self.BoutonReset.setFont(font3)
        self.ActivationPartielle = QPushButton(self.centralwidget)
        self.ActivationPartielle.setObjectName(u"ActivationPartielle")
        self.ActivationPartielle.setGeometry(QRect(30, 390, 191, 60))
        font4 = QFont()
        font4.setPointSize(15)
        self.ActivationPartielle.setFont(font4)
        self.ActivationComplete = QPushButton(self.centralwidget)
        self.ActivationComplete.setObjectName(u"ActivationComplete")
        self.ActivationComplete.setGeometry(QRect(240, 390, 191, 60))
        self.ActivationComplete.setFont(font4)
        self.Desactivation = QPushButton(self.centralwidget)
        self.Desactivation.setObjectName(u"Desactivation")
        self.Desactivation.setGeometry(QRect(30, 460, 401, 60))
        self.Desactivation.setFont(font4)
        self.codeValideCercle = QLabel(self.centralwidget)
        self.codeValideCercle.setObjectName(u"codeValideCercle")
        self.codeValideCercle.setGeometry(QRect(680, 70, 211, 31))
        self.codeValideCercle.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.Label4_10 = QLabel(self.centralwidget)
        self.Label4_10.setObjectName(u"Label4_10")
        self.Label4_10.setGeometry(QRect(560, 70, 101, 31))
        self.Label4_10.setFont(font1)
        self.courriel = QRadioButton(self.centralwidget)
        self.courriel.setObjectName(u"courriel")
        self.courriel.setGeometry(QRect(450, 400, 82, 17))
        self.courriel.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Label1.setText(QCoreApplication.translate("MainWindow", u"Chambre principale", None))
        self.Label2.setText(QCoreApplication.translate("MainWindow", u"Chambre secondaire", None))
        self.Label4.setText(QCoreApplication.translate("MainWindow", u"Porte arri\u00e8re", None))
        self.Label3.setText(QCoreApplication.translate("MainWindow", u"Porte avant", None))
        self.ChambrePrincipaleCercle.setText("")
        self.ChambreSecondaireCercle.setText("")
        self.PorteAvantCercle.setText("")
        self.PorteArriereCercle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Syst\u00e8me d'alarme Montr\u00e9al", None))
        self.Label4_2.setText(QCoreApplication.translate("MainWindow", u"Porte sous sol", None))
        self.PorteSousSolCercle.setText("")
        self.Label2_2.setText(QCoreApplication.translate("MainWindow", u"Bureau", None))
        self.BureauCercle.setText("")
        self.Label2_3.setText(QCoreApplication.translate("MainWindow", u"Salon", None))
        self.SalonCercle.setText("")
        self.SalleBillardCercle.setText("")
        self.Label4_3.setText(QCoreApplication.translate("MainWindow", u"Salle de billard", None))
        self.SalleVernisCercle.setText("")
        self.Label4_4.setText(QCoreApplication.translate("MainWindow", u"Salle de vernis", None))
        self.ReservoirEauChaudeCercle.setText("")
        self.FumeeSalleBillardCercle.setText("")
        self.Label4_5.setText(QCoreApplication.translate("MainWindow", u"fum\u00e9e salle billard", None))
        self.EntreeEauCercle.setText("")
        self.Label4_6.setText(QCoreApplication.translate("MainWindow", u"R\u00e9servoir eau chaude", None))
        self.Label4_7.setText(QCoreApplication.translate("MainWindow", u"Entr\u00e9e d'eau", None))
        self.Label4_8.setText(QCoreApplication.translate("MainWindow", u"fum\u00e9e atelier", None))
        self.FumeeAtelierCercle.setText("")
        self.SystemeArmeCercle.setText("")
        self.Label4_9.setText(QCoreApplication.translate("MainWindow", u"Syst\u00e8me arm\u00e9", None))
        self.Bouton1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Bouton2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Bouton3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Bouton5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Bouton4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Bouton6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Bouton8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Bouton7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Bouton9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Bouton0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BoutonStar.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.BoutonReset.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.ActivationPartielle.setText(QCoreApplication.translate("MainWindow", u"Activation partielle", None))
        self.ActivationComplete.setText(QCoreApplication.translate("MainWindow", u"Activation compl\u00e8te", None))
        self.Desactivation.setText(QCoreApplication.translate("MainWindow", u"D\u00e9sactivation", None))
        self.codeValideCercle.setText("")
        self.Label4_10.setText(QCoreApplication.translate("MainWindow", u"Code valide", None))
        self.courriel.setText(QCoreApplication.translate("MainWindow", u"Courriel", None))
    # retranslateUi

