import sys
import mpu.io
from PyQt5 import QtCore, QtGui
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
        
        # member variables
        self.vector = [float, float] * 1000
        self.isTrackEnabled = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(660, 800)
        self.setMouseTracking(False)
        self.init_Connections()

        self.show()

    def init_Connections(self):
        self.ui.hashButton.clicked.connect(self.hashButton_Clicked)
        self.ui.randomKeyButton.clicked.connect(self.randomKeyButton_Clicked)
        self.ui.progressSlider.valueChanged.connect(self.progressSlider_Changed)
        self.ui.hashInput.textChanged.connect(self.hashInput_Changed)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton and self.isTrackEnabled:
                pos = event.pos()
                self.cursorMoved(pos.x(), pos.y())

        
        return QMainWindow.eventFilter(self, source, event)
    
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
        self.ui.blockText.setText(self.data[0]["Block"])
        

        self.ui.progressSlider.setMinimum(1)
        self.ui.progressSlider.setMaximum(len(self.data) - 1)

    def hashInput_Changed(self):
        # should hard reset the random key gen aspect of the application
        self.vector.clear()
        self.isTrackEnabled = False
        self.ui.progressBar.setValue(0)
        

    def randomKeyButton_Clicked(self):
        self.vector.clear()
        self.isTrackEnabled = True

    def progressSlider_Changed(self):
        current = self.data[self.ui.progressSlider.value()]

        buffers = current["Loop"]["Buffers"]
        word = current["Loop"]["Word"]
        f = current["Loop"]["f"]
        g = current["Loop"]["g"] 
        id = current["Loop"]["Id"]
        
        # update the ui 
        self.ui.aBufferVal.setText(str(hex(buffers[0])))
        self.ui.bBufferVal.setText(str(hex(buffers[1])))
        self.ui.cBufferVal.setText(str(hex(buffers[2])))
        self.ui.dBufferVal.setText(str(hex(buffers[3])))
        self.ui.fBufferVal.setText(str(f))
        self.ui.gBufferVal.setText(str(g))
        self.ui.workingWordText.setText(str(word))
        self.ui.loopCountLabel.setText('Loop Count: ' + str(id))
    
    def cursorMoved(self, x, y):
        if len(self.vector) == 1000:
            self.isTrackEnabled is False
            self.mouse_vector_acquired()
            return

        # check the cursor is within the bounds of the groupBox
        rect = self.ui.mouseCaptureRegion.geometry()
        xcoll = rect.x() <= x <= rect.x() + rect.width()
        ycoll = rect.y() <= y <= rect.y() + rect.height()

        if xcoll and ycoll:
            self.vector.append([x, y])
            self.ui.progressBar.setValue(len(self.vector) / 10)
    
    def mouse_vector_acquired(self):
        # called when 1000 mouse points have been collected
        # will change the input hash to a string mean of the input
        xmean = 0
        ymean = 0

        for i in range(len(self.vector)):
            xmean += self.vector[i][0]
            ymean += self.vector[i][1]
        
        xmean /= len(self.vector)
        ymean /= len(self.vector)

        self.ui.hashInput.setText("%f%f" % (xmean, ymean))

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
    app.installEventFilter(window)
    sys.exit(app.exec_())