# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_elgamal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1189, 863)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMouseTracking(False)
        Dialog.setTabletTracking(False)
        Dialog.setFocusPolicy(QtCore.Qt.TabFocus)
        Dialog.setStyleSheet("background-image: url(:/image/back_ground_copy.jpg);")
        self.anhgoc = QtWidgets.QGraphicsView(Dialog)
        self.anhgoc.setGeometry(QtCore.QRect(610, 150, 256, 256))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.anhgoc.setFont(font)
        self.anhgoc.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.anhgoc.setObjectName("anhgoc")
        self.e2 = QtWidgets.QTextEdit(Dialog)
        self.e2.setGeometry(QtCore.QRect(100, 510, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.e2.setFont(font)
        self.e2.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.e2.setObjectName("e2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 430, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 560, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(112, 112, 112);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 600, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 510, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.d = QtWidgets.QTextEdit(Dialog)
        self.d.setGeometry(QtCore.QRect(100, 600, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.d.setFont(font)
        self.d.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.d.setObjectName("d")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 470, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.banro = QtWidgets.QPlainTextEdit(Dialog)
        self.banro.setGeometry(QtCore.QRect(790, 480, 256, 256))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.banro.setFont(font)
        self.banro.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.banro.setObjectName("banro")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(160, 340, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.r = QtWidgets.QTextEdit(Dialog)
        self.r.setGeometry(QtCore.QRect(100, 690, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.r.setFont(font)
        self.r.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"")
        self.r.setObjectName("r")
        self.mahoa = QtWidgets.QPushButton(Dialog)
        self.mahoa.setGeometry(QtCore.QRect(300, 480, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.mahoa.setFont(font)
        self.mahoa.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-image: url(:/image/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.mahoa.setObjectName("mahoa")
        self.e1 = QtWidgets.QTextEdit(Dialog)
        self.e1.setGeometry(QtCore.QRect(100, 470, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.e1.setFont(font)
        self.e1.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.e1.setObjectName("e1")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(60, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(203, 185, 255);\n"
"background-image: url(:/image/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.banmat = QtWidgets.QPlainTextEdit(Dialog)
        self.banmat.setGeometry(QtCore.QRect(400, 480, 256, 256))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.banmat.setFont(font)
        self.banmat.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.banmat.setObjectName("banmat")
        self.p = QtWidgets.QTextEdit(Dialog)
        self.p.setGeometry(QtCore.QRect(100, 430, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.p.setFont(font)
        self.p.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.p.setObjectName("p")
        self.giaima = QtWidgets.QPushButton(Dialog)
        self.giaima.setGeometry(QtCore.QRect(700, 480, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.giaima.setFont(font)
        self.giaima.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-image: url(:/image/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.giaima.setObjectName("giaima")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 690, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(100, 100, 100);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(510, 150, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_13.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(238, 230, 255);\n"
"background-image: url(:/image/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setOpenExternalLinks(False)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(60, 650, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);\n"
"background-color: rgb(106, 106, 106);")
        self.label_12.setObjectName("label_12")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 130, 261, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vboxlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.khoangaunhien = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.khoangaunhien.setFont(font)
        self.khoangaunhien.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.khoangaunhien.setObjectName("khoangaunhien")
        self.vboxlayout.addWidget(self.khoangaunhien)
        self.tuychinhkhoa = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tuychinhkhoa.setFont(font)
        self.tuychinhkhoa.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.tuychinhkhoa.setObjectName("tuychinhkhoa")
        self.vboxlayout.addWidget(self.tuychinhkhoa)
        self.lammoikhoa = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lammoikhoa.setFont(font)
        self.lammoikhoa.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.lammoikhoa.setObjectName("lammoikhoa")
        self.vboxlayout.addWidget(self.lammoikhoa)
        self.refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.refresh.setObjectName("refresh")
        self.vboxlayout.addWidget(self.refresh)
        self.browser = QtWidgets.QPushButton(Dialog)
        self.browser.setGeometry(QtCore.QRect(370, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.browser.setFont(font)
        self.browser.setStyleSheet("background-image: url(:/newPrefix/C:/Users/huyna/Dropbox/PC/Downloads/Hinh-Nen-Trang-10.jpg);")
        self.browser.setObjectName("browser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">p:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Khóa bí mật:</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">d:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">e2:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">e1:</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mahoa.setText(_translate("Dialog", "Mã hóa"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Chọn ảnh</p><p align=\"center\"><br/></p></body></html>"))
        self.giaima.setText(_translate("Dialog", "Giải mã "))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">r:</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Khóa công khai:</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "Ảnh gốc"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Số ngẫu nhiên</span><span style=\" font-size:14pt; color:#ffffff;\">:</span></p><p><br/></p></body></html>"))
        self.khoangaunhien.setText(_translate("Dialog", "Khóa ngẫu nhiên"))
        self.tuychinhkhoa.setText(_translate("Dialog", "Tùy chỉnh khóa"))
        self.lammoikhoa.setText(_translate("Dialog", "Làm mới khóa"))
        self.refresh.setText(_translate("Dialog", "Refresh"))
        self.browser.setText(_translate("Dialog", "Browser"))

        self.p.toPlainText()
        self.p.clear()
        self.p.setText()
# import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())