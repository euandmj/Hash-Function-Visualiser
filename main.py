import sys
import mpu.io
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from window import Ui_MainWindow

class AppWindow(QMainWindow):
    data = []
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(640, 620)
        self.init_Connections()
        self.show()

    def init_Connections(self):
        self.ui.hashButton.clicked.connect(self.hashButton_Clicked)
        self.ui.progressSlider.valueChanged.connect(self.progressSlider_Changed)
        
    def hashButton_Clicked(self):
        import MD5
        txt = str(self.ui.hashInput.text())
        h = MD5.MD5(txt)
        self.ui.outputText.setText(MD5.toHex(h))
        
        self.data = mpu.io.read("loop.json")

        self.ui.blockText.setText(str(self.data[0]["Block"]))

        self.ui.progressSlider.setMaximum(len(self.data) - 1)

    def progressSlider_Changed(self):
        current = self.data[self.ui.progressSlider.value() + 1]
        
        buffers = current["Loop"]["Buffers"]
        f = current["Loop"]["f"]
        g = current["Loop"]["g"] 
        
        # update the ui 
        self.ui.aBufferVal.setText(str(buffers[0]))
        self.ui.bBufferVal.setText(str(buffers[1]))
        self.ui.cBufferVal.setText(str(buffers[2]))
        self.ui.dBufferVal.setText(str(buffers[3]))
        self.ui.fBufferVal.setText(str(f))
        self.ui.gBufferVal.setText(str(g))
    
def pretty_print(data, indent = 1):
    import pprint
    pp = pprint.PrettyPrinter(indent = indent)
    pp.pprint(data)

if __name__ == "__main__":
    import qdarkgraystyle
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())