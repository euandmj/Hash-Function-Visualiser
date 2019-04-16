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
        

        # css
        try:            
            with open("res\\darkorange.stylesheet.css", "r") as f:
                qstr = f.read()
                self.setStyleSheet(qstr)
        except FileNotFoundError:
            with open("darkorange.stylesheet.css", "r") as f:
                qstr = f.read()
                self.setStyleSheet(qstr)
        except:
            pass


    

    def init_Connections(self):
        self.ui.hexInputText.textChanged.connect(self.hexTextChanged)
        self.ui.decInputText.textChanged.connect(self.decTextChanged)

    

    def hexTextChanged(self):
        input = self.ui.hexInputText.text()
        
        # to dec
        try:
            hex = int(input, 16)
            self.ui.hexResultDec.setText(str(hex))
        except (ValueError, TypeError) as e:
            #print(e)
            self.ui.hexInputText.setStyleSheet("border: 1px solid red")
        except Exception:
            pass
        else:
            self.ui.hexInputText.setStyleSheet("border: 1px solid black")

        
        # to binary
        try:
            b = bin(hex)[2:]
            self.ui.hexResultBin.setText(str(b))
        except (ValueError, TypeError) as e:
            self.ui.hexInputText.setStyleSheet("border: 1px solid red")
        except Exception:
            pass
        else:
            self.ui.hexInputText.setStyleSheet("border: 1px solid black")

    def decTextChanged(self):
        input = self.ui.decInputText.text()


        # cast input string to int
        try:
            value = int(input)
        except ValueError as e:
            self.ui.decInputText.setStyleSheet("border: 1px solid red")
        else:
            # to hex
            h = hex(value)
            self.ui.decResultHex.setText(str(h))
            # to binary
            b = bin(value)
            self.ui.decResultBin.setText(str(b))

            #reset ui
            self.ui.decInputText.setStyleSheet("border: 1px solid black")



        # to binary

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())