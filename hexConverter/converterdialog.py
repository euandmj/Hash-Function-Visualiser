# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 361, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hexInputText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexInputText.sizePolicy().hasHeightForWidth())
        self.hexInputText.setSizePolicy(sizePolicy)
        self.hexInputText.setMaximumSize(QtCore.QSize(390, 16777215))
        self.hexInputText.setObjectName("hexInputText")
        self.verticalLayout.addWidget(self.hexInputText)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.hexResultBin = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexResultBin.sizePolicy().hasHeightForWidth())
        self.hexResultBin.setSizePolicy(sizePolicy)
        self.hexResultBin.setMaximumSize(QtCore.QSize(390, 16777215))
        self.hexResultBin.setReadOnly(True)
        self.hexResultBin.setObjectName("hexResultBin")
        self.verticalLayout.addWidget(self.hexResultBin)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.hexResultDec = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexResultDec.sizePolicy().hasHeightForWidth())
        self.hexResultDec.setSizePolicy(sizePolicy)
        self.hexResultDec.setMaximumSize(QtCore.QSize(390, 16777215))
        self.hexResultDec.setReadOnly(True)
        self.hexResultDec.setObjectName("hexResultDec")
        self.verticalLayout.addWidget(self.hexResultDec)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(90, 20, 221, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 221, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 361, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.decInputText = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decInputText.sizePolicy().hasHeightForWidth())
        self.decInputText.setSizePolicy(sizePolicy)
        self.decInputText.setMaximumSize(QtCore.QSize(390, 16777215))
        self.decInputText.setObjectName("decInputText")
        self.verticalLayout_2.addWidget(self.decInputText)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.decResultBin = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decResultBin.sizePolicy().hasHeightForWidth())
        self.decResultBin.setSizePolicy(sizePolicy)
        self.decResultBin.setMaximumSize(QtCore.QSize(390, 16777215))
        self.decResultBin.setReadOnly(True)
        self.decResultBin.setObjectName("decResultBin")
        self.verticalLayout_2.addWidget(self.decResultBin)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.decResultHex = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decResultHex.sizePolicy().hasHeightForWidth())
        self.decResultHex.setSizePolicy(sizePolicy)
        self.decResultHex.setMaximumSize(QtCore.QSize(390, 16777215))
        self.decResultHex.setReadOnly(True)
        self.decResultHex.setObjectName("decResultHex")
        self.verticalLayout_2.addWidget(self.decResultHex)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 361, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.binInputText = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binInputText.sizePolicy().hasHeightForWidth())
        self.binInputText.setSizePolicy(sizePolicy)
        self.binInputText.setMaximumSize(QtCore.QSize(390, 16777215))
        self.binInputText.setObjectName("binInputText")
        self.verticalLayout_3.addWidget(self.binInputText)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.bin_decResult = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bin_decResult.sizePolicy().hasHeightForWidth())
        self.bin_decResult.setSizePolicy(sizePolicy)
        self.bin_decResult.setMaximumSize(QtCore.QSize(390, 16777215))
        self.bin_decResult.setReadOnly(True)
        self.bin_decResult.setObjectName("bin_decResult")
        self.verticalLayout_3.addWidget(self.bin_decResult)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.bin_hexResult = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bin_hexResult.sizePolicy().hasHeightForWidth())
        self.bin_hexResult.setSizePolicy(sizePolicy)
        self.bin_hexResult.setMaximumSize(QtCore.QSize(390, 16777215))
        self.bin_hexResult.setReadOnly(True)
        self.bin_hexResult.setObjectName("bin_hexResult")
        self.verticalLayout_3.addWidget(self.bin_hexResult)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(90, 20, 221, 20))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "In base 2 binary:"))
        self.label_3.setText(_translate("Dialog", "In base 10 decimal:"))
        self.label.setText(_translate("Dialog", "Enter a hexadecimal value to convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Hex"))
        self.label_4.setText(_translate("Dialog", "Enter a decimal value to convert"))
        self.label_5.setText(_translate("Dialog", "In base 2 binary:"))
        self.label_6.setText(_translate("Dialog", "In base 16 hexadecimal:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Decimal"))
        self.label_7.setText(_translate("Dialog", "In base 10 decimal:"))
        self.label_8.setText(_translate("Dialog", "In base 16 hexadecimal:"))
        self.label_9.setText(_translate("Dialog", "Enter a binary value to convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Binary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

