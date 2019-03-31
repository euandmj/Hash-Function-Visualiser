import sys
import os
import mpu.io
import psutil
import mpu.io
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from window import Ui_MainWindow
from HashLib import MD5, SHA1



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

        self.metadata = []

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
        self.ui.launchVisualiserButton.clicked.connect(self.launchVisualTab)
        self.ui.hashCombo.currentIndexChanged.connect(self.hashSelectionChanged)

    def init_Interface(self):
        # css
        with open("res/darkorange.stylesheet.css", "r") as f:
            qstr = f.read()
            self.setStyleSheet(qstr)

        # load hash meta file
        self.metadata = mpu.io.read("hash_meta.json")
        self.hashSelectionChanged()


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
        # check if a file was chosen and note qdialog exited
        if filen[1] != '':
            self.runHash(filen, True)

    def exportButton_Clicked(self):
        pass
    
    def launchVisualTab(self):
        # get the current index of the scrollbar
        # export the import data to curr_loop.json
        # while the process is running, "pause this program"
        filen = "curr_loop.json"
        
        # visualiser needs:
        # A B C D
        # M T S
        current = self.data[self.ui.progressSlider.value()]       
        
        visualdata = current["VisualData"]

        if os.path.isfile(filen):
            os.remove(filen)
        mpu.io.write(filen, visualdata)


        os.system("Visualiser.exe")

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

    def hashSelectionChanged(self):
        comboIndex = self.ui.hashCombo.currentIndex()

        if comboIndex == 0:
            # md5 chosen
            # update constants area
            self.updateConstantRegion(self.metadata["MD5"])

        elif comboIndex == 1:
            # sha1 chosen
            pass

    def updateConstantRegion(self, data):
        self.ui.sineTable.setRowCount(16)
        self.ui.sineTable.setColumnCount(2)
        
        from PyQt5.QtWidgets import QHeaderView
        header = self.ui.sineTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        for i in range(16):
            # row from the json file
            row = data["Sine Table"][str(i)]
            split = row.split(',')
            self.ui.sineTable.setItem(i, 0, QTableWidgetItem(str(i).upper()))
            self.ui.sineTable.setItem(i, 1, QTableWidgetItem(split[0]))

            self.ui.sineTable.setItem(i+1, 0, QTableWidgetItem(str(i+1).upper()))
            self.ui.sineTable.setItem(i+1, 1, QTableWidgetItem(split[1]))
            
            self.ui.sineTable.setItem(i+2, 0, QTableWidgetItem(str(i+2).upper()))
            self.ui.sineTable.setItem(i+2, 1, QTableWidgetItem(split[2]))
            
            self.ui.sineTable.setItem(i+3, 0, QTableWidgetItem(str(i+3).upper()))
            self.ui.sineTable.setItem(i+3, 1, QTableWidgetItem(split[3]))

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