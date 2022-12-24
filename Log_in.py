import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5.uic import loadUi
import pymysql
from Project_Pack import choice
class Myfirstprg(QDialog):

    def __init__(self):
        super(Myfirstprg,self).__init__()
        loadUi("login.ui",self)
        self.btn1.clicked.connect(self.li)



    def li(self):

        db = pymysql.connect(host="localhost", password="123", database="quiz_program", user="shivamkumar")
        cur = db.cursor()
        if(len(self.t1.text())==0):
            QMessageBox.about(self,"Error","Please Enter player_id")

        else:

            pl= self.t1.text()
            pas=self.t2.text()
            cur.execute("select * from new_user where e_mail='" +pl+"' and password='"+pas+"'")
            n = cur.rowcount

            if (n == 0):
                QMessageBox.about(self, "Interface", "Player_id not Exits")
            else:
                obj1=choice.shivam(pl)
                obj1.show()
                obj1.exec_()
            db.close()

# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())