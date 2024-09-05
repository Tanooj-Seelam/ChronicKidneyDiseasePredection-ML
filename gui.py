import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont, QPixmap
from PyQt5.QtCore import Qt, QLine

import chronic
import warnings

warnings.filterwarnings('ignore')


class Kidneys(QWidget):

    def __init__(self) -> None:
        super(Kidneys, self).__init__()
        self.sub_head = QLabel("Patient's Details")
        self.sub_head.setFont(QFont("Times", 24, weight=QFont.Bold))
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.t0 = QLabel("Patient's Name:")
        self.t1 = QLabel("BP:")
        self.t2 = QLabel("SOD:")
        self.t3 = QLabel("POT:")
        self.t4 = QLabel("Pcv:")
        self.t5 = QLabel("Rbcc:")
        self.r1 = QLabel("(70-180)")
        self.r2 = QLabel("(80-140)")
        self.r3 = QLabel("(10-50)")
        self.r4 = QLabel("(15-276)")
        self.r5 = QLabel("(10-50)")
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.clbtn = QPushButton("CLEAR")
        self.clbtn.setFixedWidth(100)
        self.submit = QPushButton("SUBMIT")
        self.submit.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.label = QLabel(self)
        self.initui()

    def initui(self) -> None:
        """ The gui is created and widgets elements are set here """
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l0.setToolTip("Enter name here")
        self.l1.setToolTip("")
        self.l2.setToolTip("80-140")
        self.l3.setToolTip("10-50")
        self.l4.setToolTip("15-276")
        self.l5.setToolTip("")
        self.l0.setFixedSize(265, 30)
        self.l1.setFixedSize(40, 30)
        self.l2.setFixedSize(40, 30)
        self.l3.setFixedSize(40, 30)
        self.l4.setFixedSize(40, 30)
        self.l5.setFixedSize(40, 30)
        self.h0.addWidget(self.t0)
        self.h0.addWidget(self.l0)
        self.v1_box.addLayout(self.h0)
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)
        self.v1_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
        self.h4.addWidget(self.r4)
        self.v1_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.h5.addWidget(self.r5)
        self.v1_box.addLayout(self.h5)
        self.h6 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Click to check if patient has Kidneys Problem")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h6.addWidget(self.submit)
        self.h6.addWidget(self.clbtn)
        self.v1_box.addLayout(self.h6)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(40)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("About")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times", 24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel(" ")
        self.details.setFont(QFont("Arial", 14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details = QLabel("Fill details and press submit to see details.")
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.report_subhead.setText("About")
        self.model_details.setText("Fill details and press submit to see details.")
        self.results.setText(" ")
        self.details.setText("")
        # print(self.frameGeometry().width())
        # print(self.frameGeometry().height())

    def test_input(self) -> None:
        """ test for Kidneys"""
        my_dict = {"B": float(self.l1.text()), "C": float(self.l2.text()), "D": float(self.l3.text()),
                   "E": float(self.l4.text()), "F": float(self.l5.text())}
        output = chronic.check_input(my_dict)
        # print(self.output)
        # self.setFixedSize(850, 342)
        self.report_subhead.setText("Result")
        self.model_details.setText("")
        #
        if output == 0:
            self.results.setText("Diagnosis suggests that patient does not suffers from Kidney Disease.")
        else:
            self.results.setText(
                "Our diagnosis suggests patient does suffer from Kidney Disease.\nPlease get checked soon.")
        self.results.setFont(QFont("Arial", 14, weight=QFont.Bold))

    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(898, 422)
        self.setWindowTitle("Kidneys Detection")
        self.label.setPixmap(QPixmap('kidney.jpg'))
        self.label.setGeometry(0, 0, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a_window = Kidneys()
    a_window.mwindow()
    sys.exit(app.exec_())
