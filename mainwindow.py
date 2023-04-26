# This Python file uses the following encoding: utf-8
import logging
import sys

import BAC0
import ui_form

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO)
logging.disable(logging.DEBUG)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.readPointsBtn.clicked.connect(self.readPoints)
        self.ui.connectBtn.clicked.connect(self.prepareNet)
        self.ui.discoverBtn.clicked.connect(self.discoverDevices)
        self.ui.devicesText.itemDoubleClicked.connect(self.defineController)
        self.ui.pointslistWidget.itemDoubleClicked.connect(self.readProperty)

    def prepareNet(self):
        if self.ui.connectBtn.text() == "Connect":
            self.bac = BAC0.connect(self.ui.server.text())
            self.ui.connectBtn.setText("Disconnect")
            self.ui.serverLabel.setText("Connected")
        else:
            self.bac.disconnect()
            self.ui.connectBtn.setText("Connect")
            self.ui.serverLabel.setText("Disconnected")
        #
        # with open('test.log', 'r') as f:
        #     self.ui.loggerText.setText(f.read())

    def discoverDevices(self):
        all =  self.bac.whois()
        self.ui.devicesText.clear()
        for i in all:
            self.ui.devicesText.addItem(str(i))

    def defineController(self):
        controller = str(self.ui.devicesText.currentItem().text())
        controller = controller.replace('(', '')
        controller = controller.replace(')', '')
        device = controller.split(',')
        print(device)
        self.ui.ipLine.setText(device[0].replace('\'', ''))
        self.ui.deviceId.setText(device[1])
        self.ctr = BAC0.device(device[0].replace('\'', ''), int(device[1]), self.bac)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.updateValue)
        self.timer.start()
        # with open('test.log', 'r') as f:
        #     self.ui.loggerText.setText(f.read())

    def readPoints(self):
        # for x in self.ctr.points[int(self.ui.object.text())].bacnet_properties:
        #     self.ui.dataText.append(str(x))
        # self.ui.dataText.setText(str(self.ctr.points[int(self.ui.object.text())].bacnet_properties).replace(',', '\n'))
        self.ui.pointslistWidget.clear()
        for i in range(0, len(self.ctr.points)):
            self.ui.pointslistWidget.addItem(f'NUM : {i} #'+(str(self.ctr.points[i])))

    def readProperty(self):
        # selctedItem = self.ui.pointslistWidget.currentItem()
        properties = self.ctr.points[int(self.ui.pointslistWidget.currentRow())].bacnet_properties
        self.ui.presentValueshow.setText(str(properties['presentValue']))
        self.ui.dataText.setText(str(self.ctr.points[int(self.ui.pointslistWidget.currentRow())].bacnet_properties).replace(',', '\n'))


    def updateValue(self):
        if self.bac and self.ctr:
            self.ui.pointslistWidget.clear()
            for i in range(0, len(self.ctr.points)):
                self.ui.pointslistWidget.addItem(f'NUM : {i} #' + (str(self.ctr.points[i])))
            self.readProperty()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
