import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
from Project_Pack import prg1 , Log_in ,admin_lgn
class Myfirstprg(QDialog):
    def __init__(self):
        super(Myfirstprg,self).__init__()
        loadUi("first_page.ui",self)
        self.btn1.clicked.connect(self.NU)
        self.btn2.clicked.connect(self.Lin)
        self.btn3.clicked.connect(self.Adm)
        self.btn4.clicked.connect(self.finish)

    def NU(self):
        obj1=prg1.Myfirstprg()
        obj1.show()
        obj1.exec_()

    def Lin(self):
        obj2=Log_in.Myfirstprg()
        obj2.show()
        obj2.exec_()

    def Adm(self):
        obj1=admin_lgn.Myfirstprg()
        obj1.show()
        obj1.exec_()

    def finish(self):
        self.close()
        QMessageBox.about(self,"Thanks ","Thanks for Visting here \n Have a nice day")

app=QApplication(sys.argv)
n=Myfirstprg()
n.show()
sys.exit(app.exec_())