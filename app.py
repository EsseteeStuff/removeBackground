# Remove Image Background using Python
from rembg import remove 
from PIL import Image 
import sys
import mainForm
from PyQt5.QtCore import QStandardPaths, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QFileDialog, QDialog
from PyQt5.QtGui import QPixmap
from aboutDialog import Ui_Dialog



class CustomDialog(QDialog,Ui_Dialog):  # Inherit from both QDialog and the generated UI class
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call the setupUi method from the generated UI class
        self.btnOK.clicked.connect(self.close)


class Window(QMainWindow, mainForm.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        self.saveDir = QStandardPaths.locate(QStandardPaths.GenericDataLocation, str(), QStandardPaths.LocateDirectory) + "RemoveBackground/"
        myDir = QDir()
        if not myDir.exists(self.saveDir):
            myDir.mkpath(self.saveDir)
        self.actionQuit.triggered.connect(self.exitApp)
        self.actionLoad_image.triggered.connect(self.loadImage)
        self.actionSave_Image.triggered.connect(self.saveImage)
        self.actionAbout.triggered.connect(self.about)

    def about(self):
        dialog = CustomDialog()
        dialog.exec_()

    def loadImage(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
        print(file_path)

        if file_path:
            pixmap = Image.open(file_path)
            self.lblInputPicture.setPixmap(QPixmap(file_path))
            self.lblInputPicture.setScaledContents(True)
            output_path = self.saveDir + "output.png"
            output = remove(pixmap)
            output.save(output_path)
            self.lblOutputPicture.setPixmap(QPixmap(output_path))
            self.lblInputPicture.setScaledContents(True)

    def saveImage(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;BMP Files (*.bmp);;All Files (*)", options=options)

        if file_path:
            self.pixmap = self.lblOutputPicture.pixmap()
            self.pixmap.save(file_path)

    def exitApp(self):
        sys.exit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def txtMessage(self):
        msg = QMessageBox()
        msg.setWindowTitle("This is a message")
        msg.setText("\nShowing Messages.\n\nVery easy!")
        msg.exec_()
        
    def closeApp(self):
        exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())






'''input_path = 'cl.jpg'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)'''
