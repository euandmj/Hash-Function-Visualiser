import sys
from PyQt5 import QtWidgets
from window import Ui_MainWindow
import MD5

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()




ui.setupUi(MainWindow)

# do all modification to the ui file before .show
MainWindow.show()
sys.exit(app.exec_())
