import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import pymysql
from Project_Pack import admin

class Myfirstprg(QDialog):
    def __init__(self):
        super(Myfirstprg, self).__init__()
        loadUi("admin_lgin.ui", self)
        self.btn1.clicked.connect(self.admin)

    def admin(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()

        usid= self.t1.text()
        pas= self.t2.text()

        cur.execute("select * from admin where user_id='"+usid+"' and password='"+pas+"';")
        n=cur.rowcount

        if(n==0):
            QMessageBox.about(self,"Oops...","Sorry Admin is not found")


        else:
            obj1=admin.Myfirstprg(usid)
            obj1.show()
            obj1.exec_()



# app = QApplication(sys.argv)
# n = Myfirstprg()
#
# n.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("........")