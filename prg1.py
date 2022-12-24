import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5.uic import loadUi
import pymysql
class Myfirstprg(QDialog):
    def __init__(self):
        super(Myfirstprg,self).__init__()
        loadUi("New_user.ui",self)
        self.btn1.clicked.connect(self.insert)
        self.btn2.clicked.connect(self.back)

    def back(self):
        self.close()


    def insert(self):
        db = pymysql.connect(host="localhost", password="123", database="quiz_program", user="shivamkumar")
        cur = db.cursor()

        name = self.t1.text()
        em=self.t2.text()
        pas=self.t3.text()
        gen = ""
        if (self.rb1.isChecked()):
            gen = "M"
        if (self.rb2.isChecked()):
            gen = "F"

        # cpas=self.t4.text()

        mobile=self.t5.text()
        age=self.t6.text()
        ct=self.t7.text()

        cur.execute("insert into new_user (name,e_mail,password,mobile_no,age,gender,city) values('"+name+"','"+em+"','"+pas+"','"+mobile+"','"+age+"','"+gen+"','"+ct+"');")
        db.commit()
        QMessageBox.about(self, "Inserting data", "Data Inserted Successfully")

        db.close()


# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())