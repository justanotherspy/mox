from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_mox(object):
    def setupUi(self, mox):
        mox.setObjectName("mox")
        mox.resize(800, 600)

        self.progressBar = QtWidgets.QProgressBar(mox)
        self.progressBar.setGeometry(QtCore.QRect(250, 420, 300, 24))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        self.generateButton = QtWidgets.QPushButton(mox)
        self.generateButton.setGeometry(QtCore.QRect(250, 340, 300, 60))
        self.generateButton.setObjectName("generateButton")
        
        self.dollNameLineEdit = QtWidgets.QLineEdit(mox)
        self.dollNameLineEdit.setGeometry(QtCore.QRect(250, 60, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dollNameLineEdit.setFont(font)
        self.dollNameLineEdit.setPlaceholderText("Name of Doll")
        self.dollNameLineEdit.setObjectName("dollNameLineEdit")
        
        self.fileDialogButton = QtWidgets.QPushButton(mox)
        self.fileDialogButton.setGeometry(QtCore.QRect(250, 110, 300, 60))
        self.fileDialogButton.setObjectName("fileDialogButton")
        
        self.imageNameLabel = QtWidgets.QLabel(mox)
        self.imageNameLabel.setGeometry(QtCore.QRect(250, 180, 271, 16))
        self.imageNameLabel.setObjectName("imageNameLabel")
        
        self.dollDescription = QtWidgets.QTextEdit(mox)
        self.dollDescription.setGeometry(QtCore.QRect(250, 220, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dollDescription.setFont(font)
        self.dollDescription.setAcceptRichText(False)
        self.dollDescription.setPlaceholderText("Write a short description for the doll...")
        self.dollDescription.setObjectName("dollDescription")
        
        self.startNewButton = QtWidgets.QPushButton(mox)
        self.startNewButton.setGeometry(QtCore.QRect(50, 490, 300, 60))
        self.startNewButton.setObjectName("startNewButton")
        
        self.cancelButton = QtWidgets.QPushButton(mox)
        self.cancelButton.setGeometry(QtCore.QRect(450, 490, 300, 60))
        self.cancelButton.setObjectName("cancelButton")
        
        self.instructionsLabel = QtWidgets.QLabel(mox)
        self.instructionsLabel.setGeometry(QtCore.QRect(30, 60, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setObjectName("instructionsLabel")

        self.retranslateUi(mox)
        QtCore.QMetaObject.connectSlotsByName(mox)

    def retranslateUi(self, mox):
        _translate = QtCore.QCoreApplication.translate
        mox.setWindowTitle(_translate("mox", "Mox QR Code generator"))
        self.generateButton.setText(_translate("mox", "Generate Code and Upload image"))
        self.fileDialogButton.setText(_translate("mox", "Choose image file"))
        self.imageNameLabel.setText(_translate("mox", "Image name:"))
        self.startNewButton.setText(_translate("mox", "Start over new"))
        self.cancelButton.setText(_translate("mox", "Cancel and close"))
        instructions = "Instructions:\nStep 1: Name doll\nStep 2: Choose image\nStep 3: Write a description\nStep 4: Click generate"
        self.instructionsLabel.setText(_translate("mox", instructions))

def main():
    app = QtWidgets.QApplication(sys.argv)
    mox = QtWidgets.QWidget()
    ui = Ui_mox()
    ui.setupUi(mox)
    mox.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()