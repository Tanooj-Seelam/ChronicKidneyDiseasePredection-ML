import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QDialog)
from PyQt5.QtGui import QPixmap


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        layout = QGridLayout()

        label_name = QLabel('<font size="5"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please Enter Your Username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
        layout.setRowMinimumHeight(2, 75)

        label_password = QLabel('<font size="5"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please Enter Your Password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)
        layout.setRowMinimumHeight(2, 75)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Admin' and self.lineEdit_password.text() == '000':

            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password / Username')
            msg.exec_()

    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(600, 400)
        self.setWindowTitle("Kidney Disease Detection")
        self.label.setPixmap(QPixmap('kidney.jpg'))
        self.label.setGeometry(0, 0, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.mwindow()
    form.show()

    sys.exit(app.exec_())
