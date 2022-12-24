import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5.uic import loadUi
import pymysql
class Myfirstprg(QDialog):
    EMAIL=" "
    def __init__(self,ema2):
        self.EMAIL=ema2
        super(Myfirstprg,self).__init__()
        loadUi("score_board.ui",self)

        self.btn3.clicked.connect(self.bacK)
        self.Score1()
    def bacK(self):
        self.close()

    def Score1(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()
        cur.execute("select * from new_user where e_mail='" + self.EMAIL + "'")
        res = cur.fetchall()

        for r in res:
            self.t1.setText(r[1])
            self.t2.setText(r[8])

        db.close()

#
# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())