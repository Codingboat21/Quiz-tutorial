import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
from PyQt5 import QtWidgets
from Project_Pack import admin_pass , score_his ,question_bank ,usinfo , QuestionB

class Myfirstprg(QDialog):
    Usrid=" "
    def __init__(self,usrid):
        self.Usrid=usrid
        super(Myfirstprg,self).__init__()
        loadUi("Admin2.ui",self)

        self.btn6.clicked.connect(self.finish)
        self.btn5.clicked.connect(self.Chnpas)
        self.btn4.clicked.connect(self.scorehis)
        self.btn1.clicked.connect(self.questions)
        self.btn2.clicked.connect(self.usrinfo)
        self.btn3.clicked.connect(self.Ques)

    def Ques(self):
        obj1=QuestionB.Myfirstprg()
        obj1.show()
        # wodgets= QtWidgets.QStackedWidget()
        # wodgets.addWidget(obj1)
        # wodgets.setFixedHeight(850)
        # wodgets.setFixedWidth(1120)
        # wodgets.show()
        obj1.exec_()

    def usrinfo(self):
        obj1=usinfo.Myfirstprg()
        obj1.show()
        obj1.exec_()


    def questions(self):
        obj2=question_bank.Myfirstprg()
        obj2.show()
        obj2.exec_()

    def scorehis(self):
        obj1=score_his.Myfirstprg()
        obj1.show()
        obj1.exec_()

    def Chnpas(self):
        obj2=admin_pass.Myfirstprg()
        obj2.show()
        obj2.exec_()

    def finish(self):
        self.close()
        QMessageBox.about(self,"Sign out","Sign Out Successfully")

# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())