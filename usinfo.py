import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import pymysql

class Myfirstprg(QDialog):
    def __init__(self):
        super(Myfirstprg, self).__init__()
        loadUi("users_info.ui", self)
        self.btn1.clicked.connect(self.Close)

        self.usinfo()
    def Close(self):
        self.close()

    def usinfo(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()

        row=0

        cur.execute("select * from new_user")
        result=cur.fetchall()

        self.tw.setRowCount(len(result))

        for r in result:
            self.tw.setItem(row,0,QtWidgets.QTableWidgetItem(r[1]))
            self.tw.setItem(row,1,QtWidgets.QTableWidgetItem(r[2]))
            self.tw.setItem(row,2,QtWidgets.QTableWidgetItem(r[3]))
            self.tw.setItem(row,3,QtWidgets.QTableWidgetItem(r[4]))
            self.tw.setItem(row,4,QtWidgets.QTableWidgetItem(r[5]))
            self.tw.setItem(row,5,QtWidgets.QTableWidgetItem(r[6]))
            self.tw.setItem(row,6,QtWidgets.QTableWidgetItem(r[7]))
            self.tw.setItem(row,7,QtWidgets.QTableWidgetItem(r[8]))
            row+=1

        db.close()


# app = QApplication(sys.argv)
# n = Myfirstprg()
# n.show()
# sys.exit(app.exec_())
