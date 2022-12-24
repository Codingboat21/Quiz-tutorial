import  sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi
import pymysql
class Myfirstprg(QDialog):

    score=0
    em1=" "
    pos=1


    def ans(self):
        db = pymysql.connect(user="shivamkumar", host="localhost", password="123", database="quiz_program")
        cur = db.cursor()

        answer=""


        if(self.r1.isChecked()):
            answer="A"

        if (self.r2.isChecked()):
            answer="B"

        if (self.r3.isChecked()):
            answer = "C"

        if (self.r4.isChecked()):
            answer = "D"

        cur.execute("select * from questions where Que_no= " + str(self.pos))

        result=cur.fetchall()


        for res in result:
            correct_ans=res[6]


        if(answer==correct_ans):
            QMessageBox.about(self,"Result","Correct Answer")
            self.score+=1
        else:
            QMessageBox.about(self,"Result","Wrong Answer!\nCorrect Answer should be "+ correct_ans)


        self.t3.setText(str(self.score))

        cur.execute("update new_user set score ='" + str(self.score) + "' where e_mail='" + self.em1 + "';")
        db.commit()

        db.close()


        self.pos+=1
        self.quiz()


    def quiz(self):
        db=pymysql.connect(user="shivamkumar",host="localhost",password="123",database="quiz_program")
        cur=db.cursor()


        cur.execute("select * from questions where Que_no= "+str(self.pos))

        result=cur.fetchall()
        for res in result:
            self.l1.setText(res[1])
            self.r1.setText(res[2])
            self.r2.setText(res[3])
            self.r3.setText(res[4])
            self.r4.setText(res[5])

        db.close()
    def back(self):
        self.close()

    def __init__(self,emal):
        self.em1=emal
        super(Myfirstprg,self).__init__()
        loadUi("Quiz_page.ui",self)
        self.btn5.clicked.connect(self.ans)
        self.btn6.clicked.connect(self.back)


        self.pos=1
        self.quiz()


# app=QApplication(sys.argv)
# n=Myfirstprg()
# n.show()
# sys.exit(app.exec_())