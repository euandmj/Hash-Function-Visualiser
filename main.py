import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from window import Ui_MainWindow
import MD5

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

 #def OutputHash(self):
 #       import MD5

 #       h = MD5.MD5(b"abc")
 #       self.outputText.setText(str(h))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(640, 500)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    # Modify runtime values here
    ui.hashButton.clicked.connect(ui.OutputHash)
    # do all modification to the ui file before .show
    MainWindow.show()
    sys.exit(app.exec_())
