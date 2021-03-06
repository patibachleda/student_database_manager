# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'id_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtCore import Qt
import requests
import urllib
from student_account import StudentAccount
from db_manager import DBManager


class UiSearch(object):
    def load_image(self):
        my_image = QImage()
        my_image.loadFromData(requests.get("http://cse2050.drfitz.fit/data/avatars/" + self.photo_text.text()).content)
        self._pic_label = QLabel(self.pic_label)  # chose a parent, such as a layout where you want to show your image
        w = 191  # set a value for your scaled width here
        h = 231  # set a value for your scaled height here

        pixmap = QPixmap.fromImage(my_image)  # Scale the image to fit your label

        # It's a good idea to keep the aspect ratio so your image does not get distorted
        scaled_img = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self._pic_label.setPixmap(scaled_img)
        self._pic_label.show()

# calls db to return a list of info using search_by_id
    def get_data(self):
        text = self.line_edit.text()
        db = DBManager()
        db.open_connection()
        result = db.search_by_id(text)
        db.close_connection()

        # sets the field to returned result from search_by_id
        if result:
            self.first_name_text.setText(result[0][1])
            self.last_name_text.setText(result[0][2])
            self.email_text.setText(result[0][3])
            self.year_text.setText(str(result[0][4]))
            self.photo_text.setText(result[0][5])
            self.load_image()
        else:
            show_msg = QMessageBox(QMessageBox.Critical, 'Error',
                                   "Could not find a student with that ID",
                                   QMessageBox.Ok)
            show_msg.exec_()

    def setup_ui(self, search):
        search.setObjectName("search")
        search.resize(609, 572)
        self.label_7 = QtWidgets.QLabel(search)
        self.label_7.setGeometry(QtCore.QRect(90, 110, 81, 21))
        self.label_7.setStyleSheet("font-size: 16px;")
        self.label_7.setObjectName("label_7")
        self.email_label = QtWidgets.QLabel(search)
        self.email_label.setGeometry(QtCore.QRect(250, 270, 81, 20))
        self.email_label.setStyleSheet("font-size: 14px;")
        self.email_label.setObjectName("email_label")
        self.last_name_label = QtWidgets.QLabel(search)
        self.last_name_label.setGeometry(QtCore.QRect(250, 230, 81, 20))
        self.last_name_label.setStyleSheet("font-size: 14px;")
        self.last_name_label.setObjectName("last_name_label")
        self.photo_text = QtWidgets.QLabel(search)
        self.photo_text.setGeometry(QtCore.QRect(380, 350, 191, 21))
        self.photo_text.setAccessibleName("")
        self.photo_text.setStyleSheet("font-size: 14px;")
        self.photo_text.setText("")
        self.photo_text.setObjectName("photo_text")
        self.line_edit = QtWidgets.QLineEdit(search)
        self.line_edit.setGeometry(QtCore.QRect(220, 110, 311, 21))
        self.line_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_edit.setText("")
        self.line_edit.setObjectName("line_edit")
        self.line = QtWidgets.QFrame(search)
        self.line.setGeometry(QtCore.QRect(30, 60, 551, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.first_name_label = QtWidgets.QLabel(search)
        self.first_name_label.setGeometry(QtCore.QRect(250, 190, 81, 20))
        self.first_name_label.setStyleSheet("font-size: 14px;")
        self.first_name_label.setObjectName("first_name_label")
        self.photo_label = QtWidgets.QLabel(search)
        self.photo_label.setGeometry(QtCore.QRect(250, 350, 81, 20))
        self.photo_label.setStyleSheet("font-size: 14px;")
        self.photo_label.setObjectName("photo_label")
        self.label = QtWidgets.QLabel(search)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 41))
        self.label.setObjectName("label")
        self.year_text = QtWidgets.QLabel(search)
        self.year_text.setGeometry(QtCore.QRect(380, 310, 191, 21))
        self.year_text.setStyleSheet("font-size: 14px;")
        self.year_text.setText("")
        self.year_text.setObjectName("year_text")
        self.first_name_text = QtWidgets.QLabel(search)
        self.first_name_text.setGeometry(QtCore.QRect(380, 190, 191, 21))
        self.first_name_text.setStyleSheet("font-size: 14px;")
        self.first_name_text.setText("")
        self.first_name_text.setObjectName("first_name_text")
        self.year_label = QtWidgets.QLabel(search)
        self.year_label.setGeometry(QtCore.QRect(250, 310, 111, 20))
        self.year_label.setStyleSheet("font-size: 14px;")
        self.year_label.setObjectName("year_label")
        self.email_text = QtWidgets.QLabel(search)
        self.email_text.setGeometry(QtCore.QRect(380, 270, 191, 21))
        self.email_text.setStyleSheet("font-size: 14px;")
        self.email_text.setText("")
        self.email_text.setObjectName("email_text")
        self.last_name_text = QtWidgets.QLabel(search)
        self.last_name_text.setGeometry(QtCore.QRect(380, 230, 191, 21))
        self.last_name_text.setStyleSheet("font-size: 14px;")
        self.last_name_text.setText("")
        self.last_name_text.setObjectName("last_name_text")
        self.line_2 = QtWidgets.QFrame(search)
        self.line_2.setGeometry(QtCore.QRect(40, 470, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pic_label = QtWidgets.QLabel(search)
        self.pic_label.setGeometry(QtCore.QRect(20, 170, 191, 231))
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.push_button = QtWidgets.QPushButton(search)
        self.push_button.setGeometry(QtCore.QRect(470, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.push_button.setFont(font)
        self.push_button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
        "color: rgb(255, 255, 255);")
        self.push_button.setObjectName("push_button")
        self.push_button.setAutoDefault(False)

        # adding event listeners to the buttons and line_edit
        self.push_button.clicked.connect(search.close)
        self.line_edit.returnPressed.connect(self.get_data)

        self.retranslate_ui(search)
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslate_ui(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Search by ID"))
        self.label_7.setText(_translate("search", "Student ID"))
        self.email_label.setText(_translate("search", "Email"))
        self.last_name_label.setText(_translate("search", "Last Name"))
        self.first_name_label.setText(_translate("search", "First Name"))
        self.photo_label.setText(_translate("search", "Photo"))
        self.label.setText(_translate("search", "<html><head/><body><p><span style=\" font-size:16pt;\">Search by ID</span></p></body></html>"))
        self.year_label.setText(_translate("search", "Admittance Year"))
        self.push_button.setText(_translate("search", "Exit"))
