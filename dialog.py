import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from converterdialog import Ui_Dialog



class AppWindow(QDialog):
    


    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.setFixedSize(400, 300)
        self.ui.setupUi(self)
        self.init_Connections()
        self.ui.tabWidget.setCurrentIndex(0)
        

        # css
        try:            
            with open("res\\darkorange.stylesheet.css", "r") as f:
                qstr = f.read()
                self.setStyleSheet(qstr)
        except FileNotFoundError:
            with open("darkorange.stylesheet.css", "r") as f:
                qstr = f.read()
                self.setStyleSheet(qstr)


    

    def init_Connections(self):
        self.ui.hexInputText.textChanged.connect(self.hexTextChanged)
        self.ui.decInputText.textChanged.connect(self.decTextChanged)
        self.ui.binInputText.textChanged.connect(self.binTextChanged)

    

    def hexTextChanged(self):
        input = self.ui.hexInputText.text()
       
        try:
            _hex = int(input, 16)
        except (ValueError, TypeError) as e:
            #print(e)
            self.ui.hexInputText.setStyleSheet("border: 1px solid red")
        except Exception as e:
            print(e)
        else: 
            # to dec
            self.ui.hexResultDec.setText(str(_hex))

            # to binary
            b = bin(_hex)[2:]
            self.ui.hexResultBin.setText(str(b))

            self.ui.hexInputText.setStyleSheet("border: 1px solid black")
        

    def decTextChanged(self):
        input = self.ui.decInputText.text()


        # cast input string to int
        try:
            value = int(input)
        except ValueError as e:
            self.ui.decInputText.setStyleSheet("border: 1px solid red")
        except Exception as e:
            print(e)
        else:
            # to hex
            h = hex(value)
            self.ui.decResultHex.setText(str(h))
            # to binary
            b = bin(value)
            self.ui.decResultBin.setText(str(b))

            #reset ui
            self.ui.decInputText.setStyleSheet("border: 1px solid black")


    def binTextChanged(self):
        input = self.ui.binInputText.text()
        # to dec
        try:
            _int = int(input, 2)           

        except(ValueError, TypeError):
            self.ui.binInputText.setStyleSheet("border: 1px solid red")
        except Exception as e:
            print(e)
        else:
            #as dec
            self.ui.bin_decResult.setText(str(_int))

            # as hex
            _hex = hex(_int)
            self.ui.bin_hexResult.setText(str(_hex))
            self.ui.binInputText.setStyleSheet("border: 1px solid black")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())