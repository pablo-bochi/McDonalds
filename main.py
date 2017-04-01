# coding: UTF-8
from controller import *
from PyQt4 import QtGui
import sys
import MainWindow

class App(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.button_Save.clicked.connect(self.save_info)
        self.button_Picture.clicked.connect(self.open)

    def save_info(self):
        self.nome = self.lineEdit_NameClient.text()
        self.cpf = self.lineEdit_CPFClient.text()
        self.sex = "masculino"
        FuncionarioController.add(self.nome, self.cpf, self.fileName)

    def open(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.label_ClientPhoto.setPixmap(QtGui.QPixmap(self.fileName))


def main():
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

if __name__ == '__main__':

    print db
    db.close()