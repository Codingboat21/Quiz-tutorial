import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
from Project_Pack import  password as ps , Quiz,score_board
class shivam(QDialog):
    ema=''
    def __init__(self,pl):
        self.ema=pl
        super(shivam,self).__init__()
        loadUi("choice_page.ui",self)
        self.onstart()
        self.btn1.clicked.connect(self.quiz)
        self.btn2.clicked.connect(self.score)
        self.btn3.clicked.connect(self.password)
        self.btn4.clicked.connect(self.signout)

    def onstart(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()
        cur.execute("select * from new_user where e_mail='"+self.ema+"'")
        res=cur.fetchall()

        for r in res:
            self.lb1.setText(r[1])


        db.close()

    def score(self):
        obj2=score_board.Myfirstprg(self.ema)
        obj2.show()
        obj2.exec_()

    def quiz(self):

        obj1=Quiz.Myfirstprg(self.ema)
        obj1.show()
        obj1.exec_()
    def password(self):
        obj2=ps.Myfirstprg()
        obj2.show()
        obj2.exec_()

    def signout(self):
        self.close()
        QMessageBox.about(self,"Log_out","Log_out Successfully")


# app=QApplication(sys.argv)
# n=shivam()
# n.show()
# sys.exit(app.exec_())
