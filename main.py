import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from window import Ui_MainWindow

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(640, 500)
        self.init_Connections()
        self.show()

    def init_Connections(self):
        self.ui.hashButton.clicked.connect(self.hashButton_Clicked)
        
    def hashButton_Clicked(self):
        import MD5
        txt = str(self.ui.hashInput.text())
        h = MD5.MD5(txt)
        self.ui.outputText.setText(str(hex(h)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())