import sys
import mpu.io
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from window import Ui_MainWindow

class AppWindow(QMainWindow):
    data = []
    def __init__(self):
        # python version calls
        if(sys.version_info > (3, 0)):
            super().__init__()
        else:
            super(AppWindow, self).__init__()
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
        print(txt)
        h = MD5.MD5(txt)
        self.ui.outputText.setText(MD5.toHex(h))
        
        # clear the data struct 
        self.data.clear()
        self.data = mpu.io.read("loop.json")
    
        self.ui.blockText.clear()
        self.ui.blockText.setText(self.data[len(self.data) - 1]["Block"])
        

        self.ui.progressSlider.setMinimum(0)
        self.ui.progressSlider.setMaximum(len(self.data) - 1)

    def progressSlider_Changed(self):
        current = self.data[self.ui.progressSlider.value()]

        buffers = current["Loop"]["Buffers"]
        word = current["Loop"]["Word"]
        f = current["Loop"]["f"]
        g = current["Loop"]["g"] 
        id = current["Loop"]["Id"]

        print(self.ui.progressSlider.value())
        
        # update the ui 
        self.ui.aBufferVal.setText(str(hex(buffers[0])))
        self.ui.bBufferVal.setText(str(hex(buffers[1])))
        self.ui.cBufferVal.setText(str(hex(buffers[2])))
        self.ui.dBufferVal.setText(str(hex(buffers[3])))
        self.ui.fBufferVal.setText(str(f))
        self.ui.gBufferVal.setText(str(g))
        self.ui.workingWordText.setText(str(word))
        self.ui.loopCountLabel.setText('Loop Count: ' + str(id))
    
def pretty_print(data, indent = 1):
    import pprint
    pp = pprint.PrettyPrinter(indent = indent)
    pp.pprint(data)

if __name__ == "__main__":
    #import qdarkgraystyle
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())