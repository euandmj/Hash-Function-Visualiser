import sys
import mpu.io
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from window import Ui_MainWindow
from HashLib import MD5



class AppWindow(QMainWindow):
    data = []

    def __init__(self):
        # python version calls
        if(sys.version_info > (3, 0)):
            super().__init__()
        else:
            super(AppWindow, self).__init__()

        # member variables
        self.vector = [int, int] * 1000
        self.isTrackEnabled = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(910, 720)
        self.setMouseTracking(False)
        self.setWindowIcon(QtGui.QIcon("res/icon.png"))
        self.init_Connections()
        self.init_Interface()

        self.show()

    def init_Connections(self):
        self.ui.hashButton.clicked.connect(self.hashButton_Clicked)
        self.ui.loadFileButton.clicked.connect(self.loadFileButton_Clicked)
        self.ui.randomKeyButton.clicked.connect(self.randomKeyButton_Clicked)
        self.ui.progressSlider.valueChanged.connect(self.progressSlider_Changed)
        self.ui.exportButton.clicked.connect(self.exportButton_Clicked)

    def init_Interface(self):
        from PyQt5.QtGui import QPixmap
        from PyQt5.QtWidgets import QGraphicsPixmapItem
        pixmap = QPixmap("res/test.png")
        pixmap = pixmap.scaled(self.ui.md5graphiclabel.width(), self.ui.md5graphiclabel.height())
        self.ui.md5graphiclabel.setPixmap(pixmap)
        #item = QGraphicsPixmapItem(pixmap)
        
        # css
        with open("res/darkorange.stylesheet.css", "r") as f:
            qstr = f.read()
            self.setStyleSheet(qstr)

    def eventFilter(self, source, event):
        # event filter for a mouse movement over the mouse capture region
        # for random key gen
        if event.type() == QtCore.QEvent.MouseMove:
            if (event.buttons() == QtCore.Qt.NoButton and self.isTrackEnabled and
                    source == self.ui.mouseCaptureRegion):
                pos = event.pos()
                self.cursorMoved(pos.x(), pos.y())

        return QMainWindow.eventFilter(self, source, event)

    def hashButton_Clicked(self):
        #read in the text and send the ascii encoded byte array to the md5 function 
        msg = str(self.ui.hashInput.text())
        # msg = bytes(msg, encoding="utf-8")

        self.runHash(msg)
        # set input binary text field
        #s = ''.join("{:02x}".format(ord(x)) for x in txt)
        s = ''.join(hex(ord(x))[2:] for x in self.ui.hashInput.text())
        self.ui.inputBinaryText.clear()
        self.ui.inputBinaryText.setText("0x%s" % (s.upper()))

    def loadFileButton_Clicked(self):
        filen = QFileDialog.getOpenFileName(self, "Open File", "/home")
        self.runHash(filen, True)

    def exportButton_Clicked(self):
        pass

    def runHash(self, input, load_file=False):
        # wait cursor

        # first reset the ui
        # feed a string and run it through the hash and
        # update the user interface

        # clear the data struct
        self.data.clear()

        M = MD5()
        h = M.Hash(input, load_file)
        self.ui.outputText.setText(h.upper())

        self.data = mpu.io.read("loop.json")

        self.ui.blockText.clear()
        self.ui.blockText.setText(self.data[0]["Block"])

        self.ui.progressSlider.setMaximum(len(self.data) - 1)
        self.ui.progressSlider.setEnabled(True)
        self.ui.progressSlider.setValue(1)
        self.progressSlider_Changed()

    def randomKeyButton_Clicked(self):
        self.isTrackEnabled = False
        self.vector.clear()
        self.isTrackEnabled = True
        self.ui.mouseCaptureRegion.setTitle(
            "Move your mouse in the region beleow to generate a random key")

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
        self.ui.workingWordText.setText(str(word).upper())
        self.ui.loopCountLabel.setText('Loop Count: ' + str(id))

    def cursorMoved(self, x, y):
        if len(self.vector) == 1000:
            self.isTrackEnabled = False
            self.mouse_vector_acquired()
            return

        self.vector.append([x, y])
        self.ui.progressBar.setValue(len(self.vector) / 10)

    def mouse_vector_acquired(self):
        # called when 1000 mouse points have been collected
        # will change the input hash to a string the sum of all points

        sum = 0
        for i in range(len(self.vector)):
            sum += self.vector[i][0] + self.vector[i][1]

        self.runHash(str(sum))
        # reset the ui
        self.ui.mouseCaptureRegion.setTitle("")
        self.isTrackEnabled = False
        self.ui.inputBinaryText.clear()


def pretty_print(data, indent=1):
    import pprint
    pp = pprint.PrettyPrinter(indent=indent)
    pp.pprint(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = AppWindow()
    window.show()
    app.installEventFilter(window)
    sys.exit(app.exec_())