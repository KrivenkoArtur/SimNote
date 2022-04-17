# SimNote Project

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.Qt import QPropertyAnimation, QPoint

from Design import Ui_MainWindow

class SimNote(QMainWindow):
    def __init__(self):
        super(SimNote, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_menu.clicked.connect(self.show_leftbar)
        self.ui.btn_back.clicked.connect(self.hide_leftbar)
        self.ui.btn_open.clicked.connect(self.action_clicked)
        self.ui.btn_saveas.clicked.connect(self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Open':
            try:
                f_name = QFileDialog.getOpenFileName(self)[0]
                file = open(f_name, 'r')
                with file:
                    data = file.read()
                    self.ui.textEdit.setText(data)
            except FileNotFoundError:
                print('No such file')
        elif action.text() == 'Save as':
            f_name = QFileDialog.getSaveFileName(self)[0]
            try:
                f_name = QFileDialog.getOpenFileName(self)[0]
                file = open(f_name, 'w')
                text = self.ui.textEdit.toPlainText()
                file.write(text)
            except FileNotFoundError:
                print('No such file')
        self.hide_leftbar()

    def show_leftbar(self):
        self.animation_show = QPropertyAnimation(self)
        self.animation_show.setTargetObject(self.ui.left_frame)
        self.animation_show.setPropertyName(b'pos')
        self.animation_show.setStartValue(QPoint(-150, 0))
        self.animation_show.setEndValue(QPoint(0, 0))
        self.animation_show.setDuration(200)
        self.animation_show.start()

    def hide_leftbar(self):
        self.animation_hide = QPropertyAnimation(self)
        self.animation_hide.setTargetObject(self.ui.left_frame)
        self.animation_hide.setPropertyName(b'pos')
        self.animation_hide.setStartValue(QPoint(0, 0))
        self.animation_hide.setEndValue(QPoint(-150, 0))
        self.animation_hide.setDuration(200)
        self.animation_hide.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimNote()
    window.show()
    sys.exit(app.exec_())