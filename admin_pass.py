import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
class Myfirstprg(QDialog):
    def __init__(self):
        super(Myfirstprg,self).__init__()
        loadUi("password.ui",self)
        self.btn1.clicked.connect(self.change1)
        self.btn2.clicked.connect(self.erase)
    def erase(self):
        self.close()
    def change1(self):
        db=pymysql.connect(user="shivamkumar",password="123",database="quiz_program",host="localhost")
        cur=db.cursor()

        ema=self.t1.text()
        pas=self.t2.text()
        cpass=self.t3.text()

        cur.execute("select * from admin where user_id='" + ema + "'")
        n = cur.rowcount
        if(n==1):

            if(cpass==pas):
                cur.execute("update admin set password='"+pas+"' where user_id='"+ema+"'")
                db.commit()
                QMessageBox.about(self,"Changed password","Your password changed successfully")
            else:
                QMessageBox.about(self, "Error Occured", "Your password doesn't matched")
        else:
            QMessageBox.about(self, "Error Occured", "E_mail not found")

        db.close()
#
# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())