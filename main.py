import os
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from WidgetComponents import widgetSlideshow as slide


class MyImageViewerWidget(QFrame):

    def __init__(self, *args):

        super(MyImageViewerWidget, self).__init__(*args)
        self.setGeometry(0, 0, 800, 500)
        self.ui = slide.Ui_Form()
        self.ui.setupUi(self)

        self.img_off = 0
        self.ui.mLabel.setScaledContents(True)

        self.ti = QTimer(self)
        self.ti.setInterval(1000)
        self.ti.timeout.connect(self.next)

    def loadFiles(self):
        self.path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        self.img_off = 0
        self.images = sorted(os.listdir(self.path))

        self.ui.mLineEdit.setText(self.path + "/" + self.images[self.img_off])

        self.px = QPixmap(self.path + "/" + self.images[self.img_off])
        self.px.scaled(self.ui.mLabel.size())
        self.ui.mLabel.setPixmap(self.px)

    def next(self):
        if self.img_off < len(self.images) - 1:
            self.img_off += 1
        else:
            self.img_off = 0

        self.ui.mLineEdit.setText(self.path + "/" + self.images[self.img_off])
        self.px = QPixmap(self.path + "/" + self.images[self.img_off])
        self.px.scaled(self.ui.mLabel.size())
        self.ui.mLabel.setPixmap(self.px)

    def previous(self):
        if self.img_off > 0:
            self.img_off -= 1
        else:
            self.img_off = len(self.images) - 1

        self.ui.mLineEdit.setText(self.path + "/" + self.images[self.img_off])
        self.px = QPixmap(self.path + "/" + self.images[self.img_off])
        self.px.scaled(self.ui.mLabel.size())
        self.ui.mLabel.setPixmap(self.px)

    def animate(self):
        if self.ui.timerButton.text() == "START":
            self.ui.timerButton.setText("STOP")
            self.ti.start()
        else:
            self.ui.timerButton.setText("START")
            self.ti.stop()


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('Simple diaporama application')

        # donnée membre qui contiendra la frame associée à la widget crée par QtDesigner
        self.mDisplay = MyImageViewerWidget(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()

    w.show()
    app.exec_()
