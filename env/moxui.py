'''
Author: Daniel Schwartz
Date: April 2020
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MoxWindow(QMainWindow):
    '''
    This is the main window for the QR code generator application.
    It contains all the UI objects as well as the functions that control them.
    '''
    def __init__(self):
        super(MoxWindow, self).__init__()
        self.setupUi()
    
    def setupUi(self):
        
        # Window
        self.setObjectName("window")
        self.resize(800, 600)
        self.setWindowTitle("Mox QR Code generator")

        # Progress Bar
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(250, 420, 300, 24))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        # Generate Button
        self.generateButton = QtWidgets.QPushButton(self)
        self.generateButton.setText("Generate Code and Upload image")
        self.generateButton.setGeometry(QtCore.QRect(250, 340, 300, 60))
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(self.generateButtonClicked)
        
        # Doll Name Label
        self.dollNameLineEdit = QtWidgets.QLineEdit(self)
        self.dollNameLineEdit.setGeometry(QtCore.QRect(250, 60, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dollNameLineEdit.setFont(font)
        self.dollNameLineEdit.setPlaceholderText("Name of Doll")
        self.dollNameLineEdit.setObjectName("dollNameLineEdit")
        
        # File Dialog Button
        self.fileDialogButton = QtWidgets.QPushButton(self)
        self.fileDialogButton.setText("Choose image file")
        self.fileDialogButton.setGeometry(QtCore.QRect(250, 110, 300, 60))
        self.fileDialogButton.setObjectName("fileDialogButton")
        self.fileDialogButton.clicked.connect(self.fileDialogButtonClicked)
        
        # Image Name Label
        self.imageNameLabel = QtWidgets.QLabel(self)
        self.imageNameLabel.setText("...")
        self.imageNameLabel.setGeometry(QtCore.QRect(250, 180, 271, 16))
        self.imageNameLabel.setObjectName("imageNameLabel")
        
        # Doll Description Text Area
        self.dollDescription = QtWidgets.QTextEdit(self)
        self.dollDescription.setGeometry(QtCore.QRect(250, 220, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dollDescription.setFont(font)
        self.dollDescription.setAcceptRichText(False)
        self.dollDescription.setPlaceholderText("Write a short description for the doll...")
        self.dollDescription.setObjectName("dollDescription")
        
        # Start New Button
        self.startNewButton = QtWidgets.QPushButton(self)
        self.startNewButton.setText("Start new")
        self.startNewButton.setGeometry(QtCore.QRect(50, 490, 300, 60))
        self.startNewButton.setObjectName("startNewButton")
        self.startNewButton.clicked.connect(self.startNewButtonClicked)
        
        # Close Button
        self.closeButton = QtWidgets.QPushButton(self)
        self.closeButton.setText("Close")
        self.closeButton.setGeometry(QtCore.QRect(450, 490, 300, 60))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.closeButtonClicked)
        
        # Instructions Label
        self.instructionsLabel = QtWidgets.QLabel(self)
        self.instructionsLabel.setGeometry(QtCore.QRect(30, 60, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setObjectName("instructionsLabel")
        instructions = "Instructions:\nStep 1: Name doll\nStep 2: Choose image\nStep 3: Write a description\nStep 4: Click generate"
        self.instructionsLabel.setText(instructions)
        
        QtCore.QMetaObject.connectSlotsByName(self)


    def closeButtonClicked(self):
        '''
        This is the close button action. It simply closes the application.
        '''
        print("close")
        sys.exit()

    def startNewButtonClicked(self):
        '''
        This is the start new button action. It resets all the fields and clears the status bar.
        '''
        print("new")
        self.imageNameLabel.setText("...")
        self.dollDescription.setText("")
        self.dollNameLineEdit.setText("")

    def generateButtonClicked(self):
        '''
        This is the generate button action. It is going to collate the required data and send it to the generator.
        '''
        print("generate")


    def fileDialogButtonClicked(self):
        '''
        This is the file dialog button action. It is going to open a file picker where the user chooses the image to upload.
        '''
        print("file open")




def main():
    app = QApplication(sys.argv)
    mox = MoxWindow()
    mox.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()