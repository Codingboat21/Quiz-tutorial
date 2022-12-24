import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
class Myfirstprg(QDialog):

    def __init__(self):

        super(Myfirstprg,self).__init__()
        loadUi("question_bank.ui",self)
        self.btn1.clicked.connect(self.cancel)
        self.btn2.clicked.connect(self.question)

    def cancel(self):
        self.close()

    def question(self):
        db = pymysql.connect(user="shivamkumar", password="123", database="quiz_program", host="localhost")
        cur = db.cursor()
        if(len(self.t1.text() and self.t2.text() and self.t3.text() and self.t4.text() and self.t5.text() and self.t6.text())==0):
            QMessageBox.about(self,"Error","Please Type blank space")
        else:
            qus=self.t1.text()
            a=self.t2.text()
            b=self.t3.text()
            c=self.t4.text()
            d=self.t5.text()
            ra=self.t6.text()

            cur.execute("insert into questions (question,A,B,C,D,real_answer) values('"+qus+"','"+a+"','"+b+"','"+c+"','"+d+"','"+ra+"');")
            db.commit()
            QMessageBox.about(self,"Inserted",'Question Inserted Successfully')


        db.close()


# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())