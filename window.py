# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\Documents\Uni\year 3\diss\pyMD5\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 481, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mouseCaptureRegion = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.mouseCaptureRegion.setEnabled(True)
        self.mouseCaptureRegion.setTitle("")
        self.mouseCaptureRegion.setObjectName("mouseCaptureRegion")
        self.progressBar = QtWidgets.QProgressBar(self.mouseCaptureRegion)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(0, 170, 481, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.hashCombo = QtWidgets.QComboBox(self.mouseCaptureRegion)
        self.hashCombo.setGeometry(QtCore.QRect(0, 220, 81, 19))
        self.hashCombo.setAutoFillBackground(False)
        self.hashCombo.setMaxVisibleItems(5)
        self.hashCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.hashCombo.setObjectName("hashCombo")
        self.hashCombo.addItem("")
        self.hashCombo.addItem("")
        self.hashInput = QtWidgets.QLineEdit(self.mouseCaptureRegion)
        self.hashInput.setGeometry(QtCore.QRect(80, 220, 191, 20))
        self.hashInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hashInput.setInputMask("")
        self.hashInput.setText("")
        self.hashInput.setDragEnabled(True)
        self.hashInput.setObjectName("hashInput")
        self.hashButton = QtWidgets.QPushButton(self.mouseCaptureRegion)
        self.hashButton.setGeometry(QtCore.QRect(280, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hashButton.setFont(font)
        self.hashButton.setObjectName("hashButton")
        self.randomKeyButton = QtWidgets.QPushButton(self.mouseCaptureRegion)
        self.randomKeyButton.setGeometry(QtCore.QRect(370, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.randomKeyButton.setFont(font)
        self.randomKeyButton.setObjectName("randomKeyButton")
        self.gridLayout.addWidget(self.mouseCaptureRegion, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(500, 40, 401, 261))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(250, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(320, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(320, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.loopCountLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.loopCountLabel_4.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loopCountLabel_4.setFont(font)
        self.loopCountLabel_4.setObjectName("loopCountLabel_4")
        self.inputBinaryText = QtWidgets.QLineEdit(self.groupBox)
        self.inputBinaryText.setGeometry(QtCore.QRect(150, 20, 231, 20))
        self.inputBinaryText.setReadOnly(True)
        self.inputBinaryText.setObjectName("inputBinaryText")
        self.blockText = QtWidgets.QTextEdit(self.groupBox)
        self.blockText.setGeometry(QtCore.QRect(10, 130, 371, 111))
        self.blockText.setReadOnly(True)
        self.blockText.setObjectName("blockText")
        self.loopCountLabel_5 = QtWidgets.QLabel(self.groupBox)
        self.loopCountLabel_5.setGeometry(QtCore.QRect(10, 110, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loopCountLabel_5.setFont(font)
        self.loopCountLabel_5.setObjectName("loopCountLabel_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(200, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(320, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 310, 661, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.workingWordText = QtWidgets.QLineEdit(self.groupBox_2)
        self.workingWordText.setGeometry(QtCore.QRect(50, 50, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.workingWordText.setFont(font)
        self.workingWordText.setReadOnly(True)
        self.workingWordText.setObjectName("workingWordText")
        self.loopCountLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.loopCountLabel_2.setGeometry(QtCore.QRect(50, 30, 201, 16))
        self.loopCountLabel_2.setObjectName("loopCountLabel_2")
        self.progressSlider = QtWidgets.QSlider(self.groupBox_2)
        self.progressSlider.setEnabled(False)
        self.progressSlider.setGeometry(QtCore.QRect(100, 230, 471, 16))
        self.progressSlider.setMinimum(1)
        self.progressSlider.setMaximum(5)
        self.progressSlider.setProperty("value", 1)
        self.progressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressSlider.setObjectName("progressSlider")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 100, 311, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.aBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.aBufferVal.setFont(font)
        self.aBufferVal.setReadOnly(True)
        self.aBufferVal.setObjectName("aBufferVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aBufferVal)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.bBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bBufferVal.setFont(font)
        self.bBufferVal.setReadOnly(True)
        self.bBufferVal.setObjectName("bBufferVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bBufferVal)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.cBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cBufferVal.setFont(font)
        self.cBufferVal.setReadOnly(True)
        self.cBufferVal.setObjectName("cBufferVal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cBufferVal)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dBufferVal.setFont(font)
        self.dBufferVal.setReadOnly(True)
        self.dBufferVal.setObjectName("dBufferVal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dBufferVal)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(370, 100, 221, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.fBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fBufferVal.setFont(font)
        self.fBufferVal.setReadOnly(True)
        self.fBufferVal.setObjectName("fBufferVal")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fBufferVal)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.gBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gBufferVal.setFont(font)
        self.gBufferVal.setReadOnly(True)
        self.gBufferVal.setObjectName("gBufferVal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gBufferVal)
        self.loopCountLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.loopCountLabel.setObjectName("loopCountLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.loopCountLabel)
        self.exportButton = QtWidgets.QPushButton(self.groupBox_2)
        self.exportButton.setGeometry(QtCore.QRect(302, 280, 71, 20))
        self.exportButton.setObjectName("exportButton")
        self.outputText = QtWidgets.QLineEdit(self.groupBox_2)
        self.outputText.setGeometry(QtCore.QRect(110, 250, 451, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputText.setFont(font)
        self.outputText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputText.setAutoFillBackground(False)
        self.outputText.setAlignment(QtCore.Qt.AlignCenter)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.hashCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hashCombo.setItemText(0, _translate("MainWindow", "MD5"))
        self.hashCombo.setItemText(1, _translate("MainWindow", "SHA-1"))
        self.hashInput.setPlaceholderText(_translate("MainWindow", "Enter Input to be Hashed"))
        self.hashButton.setText(_translate("MainWindow", "Hash Message"))
        self.randomKeyButton.setText(_translate("MainWindow", "Generate Random Key"))
        self.groupBox.setTitle(_translate("MainWindow", "Constants"))
        self.label_4.setText(_translate("MainWindow", "Word Size"))
        self.label_7.setText(_translate("MainWindow", "32 bits"))
        self.label_3.setText(_translate("MainWindow", "Block Size"))
        self.label_6.setText(_translate("MainWindow", "512 bits"))
        self.loopCountLabel_4.setText(_translate("MainWindow", "Binary Message"))
        self.loopCountLabel_5.setText(_translate("MainWindow", "Padded Message"))
        self.label_5.setText(_translate("MainWindow", "Operational Block Size"))
        self.label_8.setText(_translate("MainWindow", "64 bits"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Main Loop"))
        self.loopCountLabel_2.setText(_translate("MainWindow", "Current Operational Block"))
        self.label_9.setText(_translate("MainWindow", "Buffer A"))
        self.label_10.setText(_translate("MainWindow", "Buffer B"))
        self.label_11.setText(_translate("MainWindow", "Buffer C"))
        self.label_12.setText(_translate("MainWindow", "Buffer D"))
        self.label_13.setText(_translate("MainWindow", "F"))
        self.label_14.setText(_translate("MainWindow", "g"))
        self.loopCountLabel.setText(_translate("MainWindow", "Loop Count : "))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

