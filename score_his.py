import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget
from PyQt5.uic import loadUi
import pymysql
from PyQt5 import QtWidgets


class Myfirstprg(QDialog):
    pos=1
    def __init__(self):
        super(Myfirstprg, self).__init__()
        loadUi("score_his.ui", self)

        self.btn1.clicked.connect(self.Erase)
        self.SHOW()

    def Erase(self):
        self.close()

    def SHOW(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()
        row=0

        cur.execute("select * from new_user")
        result=cur.fetchall()
        self.tw.setRowCount(len(result))

        for r in result:

            self.tw.setItem(row ,0 ,QtWidgets.QTableWidgetItem(r[1]))
            self.tw.setItem(row ,1 ,QtWidgets.QTableWidgetItem(r[8]))
            row+=1

        db.close()

# app = QApplication(sys.argv)
# n = Myfirstprg()
# n.show()
# sys.exit(app.exec_())