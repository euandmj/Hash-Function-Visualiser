import sys
import os
import mpu.io
import psutil
import subprocess
import datetime
from numpy import sin, sum
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem
from window import Ui_MainWindow
from libs.HashLib import MD5, SHA1

def openFile(file, args):
    try:
        subprocess.Popen([file, args])
    except FileNotFoundError:
        print("the file %s was not found?" % (file))
    except Exception as e:
        print(str(e))
    
def pretty_print(data, indent=1):
    import pprint
    pp = pprint.PrettyPrinter(indent=indent)
    pp.pprint(data)

class AppWindow(QMainWindow):
    # member variables
    data = []
    paddingIndex = 0  
    vector = [int, int] * 1000
    isTrackEnabled = False
    paddingDict  = {}
    # load hash meta file
    metadata = mpu.io.read("hash_meta.json")


    def __init__(self):
        # python version calls
        if(sys.version_info > (3, 0)):
            super().__init__()
        else:
            super(AppWindow, self).__init__()

      

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(910, 720)
        self.setMouseTracking(False)
        self.setWindowIcon(QtGui.QIcon("res/icon.png"))
        self.init_Connections()
        self.init_Interface()

        
        self.hashSelectionChanged()

        self.show()

    def init_Connections(self):
        self.ui.hashButton.clicked.connect(self.hashButton_Clicked)
        self.ui.loadFileButton.clicked.connect(self.loadFileButton_Clicked)
        self.ui.randomKeyButton.clicked.connect(self.randomKeyButton_Clicked)
        self.ui.progressSlider.valueChanged.connect(self.progressSlider_Changed)
        self.ui.exportButton.clicked.connect(self.exportButton_Clicked)
        self.ui.launchVisualiserButton.clicked.connect(self.launchVisualTab)
        self.ui.hashCombo.currentIndexChanged.connect(self.hashSelectionChanged)
        self.ui.actionConverter_Tool.triggered.connect(self.launchConversionTool)
        self.ui.actionKill_Children.triggered.connect(self.killChildPs)


    def init_Interface(self):
        # css
        with open("res/darkorange.stylesheet.css", "r") as f:
            qstr = f.read()
            self.setStyleSheet(qstr)

        self.ui.launchVisualiserError.hide()
        self.ui.padding_LeftArrow.setEnabled(False)
        self.ui.tabWidget.setCurrentIndex(1)


    def eventFilter(self, source, event):
        # event filter for a mouse movement over the mouse capture region
        # for random key gen
        if event.type() == QtCore.QEvent.MouseMove:
            if (event.buttons() == QtCore.Qt.NoButton and self.isTrackEnabled and
                    source == self.ui.mouseCaptureRegion):
                pos = event.pos()
                self.cursorMoved(pos.x(), pos.y())
        
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if (event.buttons() == QtCore.Qt.LeftButton and
                source == self.ui.padding_LeftArrow and
                self.ui.padding_LeftArrow.isEnabled()):
                self.paddingArrow_Clicked(0)
        
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if (event.buttons() == QtCore.Qt.LeftButton and
                    source == self.ui.padding_RightArrow and
                    self.ui.padding_RightArrow.isEnabled()):
                self.paddingArrow_Clicked(1)


        return QMainWindow.eventFilter(self, source, event)

    def getSelectedHash(self):
        if self.ui.hashCombo.currentIndex() == 0:
            return "md5"
        else:
            return "sha1"

    def hashButton_Clicked(self):
        self.ui.launchVisualiserButton.setEnabled(True)        
        #read in the text and send the ascii encoded byte array to the md5 function
        msg = str(self.ui.hashInput.text())
        # msg = bytes(msg, encoding="utf-8")

        if self.getSelectedHash() == "md5":
            # md5 selected
            m = MD5()
        elif self.getSelectedHash() == "sha1":
            # sha1 selected
            m = SHA1()
        
        self.runHash(msg, m)
        # set input binary text field
        #s = ''.join("{:02x}".format(ord(x)) for x in txt)
        # s = ''.join(hex(ord(x))[2:] for x in self.ui.hashInput.text())
        # self.ui.inputBinaryText.clear()
        # self.ui.inputBinaryText.setText("0x%s" % (s.upper()))

    def loadFileButton_Clicked(self):
        filen = QFileDialog.getOpenFileName(self, "Open File", "/home")

        if self.getSelectedHash() == "md5":
            h = MD5()
        else:
            h = SHA1()
        # check if a file was chosen and note qdialog exited
        if filen[1] != '':
            self.runHash(filen[0], h, load_file=True)

    def exportButton_Clicked(self):
        pass    

    def launchVisualTab(self):
        # if the current system is not windows....
        if os.name != 'nt':
            self.ui.launchVisualiserError.show()
            return

        # empty data - hash has not been ran yet        
        if not self.data:
            return

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

        #subprocess.Popen(["wpf_visual\Visualiser\Visualiser\\bin\Debug\Visualiser.exe", self.getSelectedHash()])
        openFile("wpf_visual\Visualiser\Visualiser\\bin\Release\Visualiser.exe", self.getSelectedHash())
    
    def killChildPs(self):
        ps = psutil.Process()
        children = ps.children(recursive=True)

        for c in children:
            c.kill()

    def launchConversionTool(self):
        #os.system("python dialog.py")
        subprocess.Popen(r"python hexConverter\dialog.py")

    def runHash(self, input, hash, load_file=False):
        # wait cursor

        # first reset the ui
        # feed a string and run it through the hash and
        # update the user interface

        # clear the data struct
        self.data.clear()

        h = hash.Hash(input, load_from_file=load_file)
        self.ui.outputText.setText(h.upper())

        self.data = mpu.io.read("loop.json")

        self.paddingDict = self.data[0]

        # self.ui.blockText.clear()
        # self.ui.blockText.setText(self.data[0]["Block"])

        self.ui.progressSlider.setMaximum(len(self.data) - 1)
        self.ui.progressSlider.setEnabled(True)
        self.ui.progressSlider.setValue(1)
        self.progressSlider_Changed()
        self.updatePaddingRegion()

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

        if len(buffers) == 5:
            self.ui.eBufferVal.setText(str(hex(buffers[4])))

    def hashSelectionChanged(self):
        if self.getSelectedHash() == "md5":
            # md5 chosen
            # update constants area
            self.updateConstantRegion(self.metadata["MD5"])

        elif self.getSelectedHash() == "sha1":
            # sha1 chosen
            self.updateConstantRegion(self.metadata["SHA1"])

        self.ui.launchVisualiserButton.setEnabled(False)

    def updateConstantRegion(self, data):
        # load sine table from data if valid
        if "Sine Table" in data:
            self.ui.sineTable.setVisible(True)
            self.ui.sineTable.setRowCount(len(data["Sine Table"]))
            self.ui.sineTable.setColumnCount(2)
        
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
        elif "Constants" in data:
            consts = data["Constants"]
            self.ui.sineTable.setVisible(True)
            self.ui.sineTable.setRowCount(len(consts))
            self.ui.sineTable.setColumnCount(2)

            header = self.ui.sineTable.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

            for i in range(len(consts)):
                self.ui.sineTable.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                self.ui.sineTable.setItem(i, 1, QTableWidgetItem(str(consts[str(i)])))
        else:
            self.ui.sineTable.setVisible(False)

        # populate register data
        registers = data["Registers"]
        self.ui.regAText.setText(registers["A"])
        self.ui.regBText.setText(registers["B"])
        self.ui.regCText.setText(registers["C"])
        self.ui.regDText.setText(registers["D"])

        # block size etc
        self.ui.digestSizeLabel_2.setText(data["Digest"])
        self.ui.digestSizeLabel_3.setText(data["Block"])
        self.ui.digestSizeLabel_4.setText(data["Rounds"])


        if "E" in registers:
            #self.ui.blockText.setGeometry(QtCore.QRect(10, 140, 211, 101))
            self.ui.label_21.setVisible(True)
            self.ui.regEText.setVisible(True)
            self.ui.regEText.setText(registers["E"])
            self.ui.label_15.setVisible(True)
            self.ui.eBufferVal.setVisible(True)
        else:
            #self.ui.blockText.setGeometry(QtCore.QRect(10, 120, 211, 121))
            self.ui.label_21.setVisible(False)
            self.ui.regEText.setVisible(False)
            self.ui.label_15.setVisible(False)
            self.ui.eBufferVal.setVisible(False)
        
       

    def updatePaddingRegion(self):
        # called upon hash and arrow click
        # depending on index, write the correct key-value to text box
        if self.paddingIndex == 0:
            self.ui.padding_BlockText.setText(
                self.paddingDict["RawBytes"]
            )
        elif self.paddingIndex == 1:
            self.ui.padding_BlockText.setText(
                self.paddingDict["RawBytes1"]
            )
        elif self.paddingIndex == 2:
            self.ui.padding_BlockText.setText(
                self.paddingDict["RawBytes0"]
            )
        elif self.paddingIndex == 3:
            self.ui.padding_BlockText.setText(
                    self.paddingDict["Block"]
            )
        
        

    def paddingArrow_Clicked(self, source):
        if not self.data:
            return
        # delta the counter
        self.paddingIndex = self.paddingIndex + 1 if source == 1 else self.paddingIndex - 1
        # disable/enable buttons based on current index
        if self.paddingIndex == 0:
            self.ui.padding_LeftArrow.setEnabled(False)
        elif self.paddingIndex == 3:
            self.ui.padding_RightArrow.setEnabled(False)
        else:
            self.ui.padding_LeftArrow.setEnabled(True)
            self.ui.padding_RightArrow.setEnabled(True)

        # source is 0 or 1 dependingg on button clicked
        labelVals = [
            "Binary of Input",
            "Append a \"1\" byte",
            "Append \"0\" bytes so that length in bits is congruent to 448 modulo 512",
            "Append 64 bit representation of original message length"
        ]

        self.ui.paddingStatusLabel.setText(labelVals[self.paddingIndex])
        self.updatePaddingRegion()
    

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
        

        _sum = sum(self.vector)
        now = datetime.datetime.now()
        val = _sum * sin(now.day + now.hour + now.second)

        self.runHash(str(val), MD5())
        # reset the ui
        self.ui.mouseCaptureRegion.setTitle("")
        self.isTrackEnabled = False
    
    def __del__(self):
        ps = psutil.Process()
        children = ps.children(recursive=True)

        for c in children:
            c.kill()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = AppWindow()
    window.show()
    app.installEventFilter(window)
    sys.exit(app.exec_())
