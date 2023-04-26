# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addressLine = QLineEdit(self.frame_2)
        self.addressLine.setObjectName(u"addressLine")
        self.addressLine.setEnabled(False)

        self.horizontalLayout.addWidget(self.addressLine)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.object = QLineEdit(self.frame_2)
        self.object.setObjectName(u"object")

        self.horizontalLayout.addWidget(self.object)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.dataText = QTextBrowser(self.frame_2)
        self.dataText.setObjectName(u"dataText")

        self.verticalLayout_3.addWidget(self.dataText)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.serverLabel = QLabel(self.frame_3)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.serverLabel)

        self.server = QLineEdit(self.frame_3)
        self.server.setObjectName(u"server")
        self.server.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.server)

        self.connectBtn = QPushButton(self.frame_3)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.connectBtn.setAutoDefault(False)
        self.connectBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.connectBtn)

        self.discoverBtn = QPushButton(self.frame_3)
        self.discoverBtn.setObjectName(u"discoverBtn")

        self.verticalLayout_4.addWidget(self.discoverBtn)

        self.ipLine = QLineEdit(self.frame_3)
        self.ipLine.setObjectName(u"ipLine")

        self.verticalLayout_4.addWidget(self.ipLine)

        self.deviceId = QLineEdit(self.frame_3)
        self.deviceId.setObjectName(u"deviceId")

        self.verticalLayout_4.addWidget(self.deviceId)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.devicesText = QListWidget(self.frame_3)
        self.devicesText.setObjectName(u"devicesText")

        self.horizontalLayout_2.addWidget(self.devicesText)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.readPointsBtn = QPushButton(self.frame_3)
        self.readPointsBtn.setObjectName(u"readPointsBtn")

        self.verticalLayout_5.addWidget(self.readPointsBtn)

        self.pointslistWidget = QListWidget(self.frame_3)
        self.pointslistWidget.setObjectName(u"pointslistWidget")

        self.verticalLayout_5.addWidget(self.pointslistWidget)

        self.presentValuelabel = QLabel(self.frame_3)
        self.presentValuelabel.setObjectName(u"presentValuelabel")
        self.presentValuelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.presentValuelabel)

        self.presentValueshow = QLabel(self.frame_3)
        self.presentValueshow.setObjectName(u"presentValueshow")
        self.presentValueshow.setMinimumSize(QSize(100, 150))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(143, 240, 164, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(153, 193, 241, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(72, 120, 82, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(95, 160, 109, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush6 = QBrush(QColor(199, 247, 209, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush9 = QBrush(QColor(239, 239, 239, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        brush10 = QBrush(QColor(202, 202, 202, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(159, 159, 159, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(184, 184, 184, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        brush13 = QBrush(QColor(118, 118, 118, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        brush14 = QBrush(QColor(247, 247, 247, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush16 = QBrush(QColor(177, 177, 177, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.presentValueshow.setPalette(palette)
        font = QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.presentValueshow.setFont(font)
        self.presentValueshow.setAlignment(Qt.AlignCenter)
        self.presentValueshow.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.presentValueshow)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1083, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.connectBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.discoverBtn.setText(QCoreApplication.translate("MainWindow", u"Discover", None))
        self.ipLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"***.***.***.***", None))
        self.deviceId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Device ID", None))
        self.readPointsBtn.setText(QCoreApplication.translate("MainWindow", u"ReadPoints", None))
        self.presentValuelabel.setText(QCoreApplication.translate("MainWindow", u"Present Value", None))
        self.presentValueshow.setText(QCoreApplication.translate("MainWindow", u"Value", None))
    # retranslateUi

