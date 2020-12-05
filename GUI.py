# coding=utf-8
import random
import time
import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QCoreApplication, QPropertyAnimation, QPoint, pyqtSlot, QTimer, pyqtSignal
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel, QScrollArea, QVBoxLayout, QWidget, qApp, QApplication, \
    QGridLayout
import FIFO
from PyQt5.QtGui import QFont, QPainter, QPen, QBrush, QPixmap, QPaintEvent, QColor
import LRU
import OPT
from NEW_GUI import Example
import images


class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.suanfa = 1
        self.init_ui()

    def init_ui(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setObjectName("清华大学得不到的学生")
        self.setWindowTitle("一只小可爱~")
        self.resize(1274, 677)
        self.label = QLabel(self)
        self.label.setWindowTitle("清华大学得不到的学生")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setGeometry(QtCore.QRect(15, 15, 1244, 647))
        self.label.setText("")
        palette = QtGui.QPalette()

        self.label.setStyleSheet("background-color: #fff;border-radius: 15px;")
        self.labelshadow = QGraphicsDropShadowEffect(self)
        self.labelshadow.setBlurRadius(15)
        self.labelshadow.setOffset(1, 1)
        self.label.setGraphicsEffect(self.labelshadow)

        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton_12 = QtWidgets.QPushButton(self)
        self.pushButton_12.setGeometry(QtCore.QRect(self.width() - 55, 29, 20, 20))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "    background:#fc625d;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#FF2D2D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    border: 1px solid #3C3C3C!important;\n"
                                         "    background:#AE0000;\n"
                                         "}")
        self.pushButton_12.clicked.connect(QCoreApplication.instance().quit)

        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(self.width() - 55 - 35, 29, 20, 20))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
                                         "    background:#35cd4b;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#00CC00;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    border: 1px solid #3C3C3C!important;\n"
                                         "    background:#009900;\n"
                                         "}")
        self.pushButton_14.clicked.connect(self.showMinimized)

        self.pushButton_15 = QtWidgets.QPushButton(self)
        self.pushButton_15.setGeometry(QtCore.QRect(70, 70, 240, 50))
        self.pushButton_15.setStyleSheet("QPushButton{background-color: #7fa6c8; font-family: 微软雅黑;" +
                                         "border: none;" +
                                         "color: #fff;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        self.pushButton_15.setText("先进先出算法-FIFO")
        self.pushButton_15.clicked.connect(self.on_click)

        self.pushButton_16 = QtWidgets.QPushButton(self)
        self.pushButton_16.setGeometry(QtCore.QRect(70, 150, 240, 50))
        self.pushButton_16.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")
        self.pushButton_16.setText("最近最久未使用算法-LRU")
        self.pushButton_16.clicked.connect(self.on_click_two)

        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(70, 230, 240, 50))
        self.pushButton_17.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")
        self.pushButton_17.setText("理想型淘汰算法-OPT")
        self.pushButton_17.clicked.connect(self.on_click_three)

        self.biaoti = QLabel(self)
        self.biaoti.setGeometry(QtCore.QRect(370, 70, 480, 50))
        self.biaoti.setStyleSheet("background-color: #f0f0f0;border-radius: 7px;")

        self.biaoti_one = QtWidgets.QPushButton(self)
        self.biaoti_one.setGeometry(QtCore.QRect(375, 75, 230, 40))
        self.biaoti_one.setStyleSheet("QPushButton{background-color: white; font-family: 微软雅黑;" +
                                      "border: none; " +
                                      "color: #000;border-radius: 5px;" +
                                      "text-align: center;" +
                                      "text-decoration: none;" +
                                      "display: inline-block;" +
                                      "font-size: 19px;" +
                                      "cursor: pointer;}"
                                      "QPushButton:hover{ "
                                      "    background-color: #9dc3e6;color: white;"
                                      "}")

        self.biaotipos = 1
        self.biaoti_two = QtWidgets.QPushButton(self)
        self.biaoti_two.setGeometry(QtCore.QRect(375, 75, 230, 40))
        self.biaoti_two.setStyleSheet("QPushButton{ font-family: 微软雅黑;" +
                                      "border: none; " +
                                      "color: #00;border-radius: 7px;" +
                                      "text-align: center;" +
                                      "text-decoration: none;" +
                                      "display: inline-block;" +
                                      "font-size: 19px;" +
                                      "cursor: pointer;}")
        self.biaoti_two.setText("手动输入")
        self.biaoti_two.clicked.connect(self.setup_ydhui)

        self.biaoti_three = QtWidgets.QPushButton(self)
        self.biaoti_three.setGeometry(QtCore.QRect(615, 75, 230, 40))
        self.biaoti_three.setStyleSheet("QPushButton{ font-family: 微软雅黑;" +
                                        "border: none; " +
                                        "color: #00;border-radius: 7px;" +
                                        "text-align: center;" +
                                        "text-decoration: none;" +
                                        "display: inline-block;" +
                                        "font-size: 19px;" +
                                        "cursor: pointer;}")
        self.biaoti_three.setText("随机生成")
        self.biaoti_three.clicked.connect(self.setup_yd)

        kuang_one = 370
        kuang_one_y = 150

        self.kuang = QLabel(self)
        self.kuang.setGeometry(QtCore.QRect(kuang_one, kuang_one_y, 480, 130))
        self.kuang.setStyleSheet("background-color: white;border-radius: 7px;")
        self.kuangshadow = QGraphicsDropShadowEffect(self)
        self.kuangshadow.setBlurRadius(30)
        cl = QColor("#eeeeee")
        self.kuangshadow.setColor(cl)
        self.kuangshadow.setOffset(0, 0)
        self.kuang.setGraphicsEffect(self.kuangshadow)

        self.edit = QtWidgets.QLineEdit(self)
        self.edit.setGeometry(QtCore.QRect(kuang_one + 20, kuang_one_y + 18, 440, 40))
        self.edit.textChanged.connect(self.set_yemian)
        self.edit.setPlaceholderText("访问页面 例如：1 2 3 4 5 6")
        self.edit.setStyleSheet("QLineEdit{background-color: #f0f0f0;border-radius: 20px;border:0px solid #000;"
                                "font-size: 18px;font-family: 微软雅黑;padding-left:16px;}")

        self.pushButton_18 = QtWidgets.QPushButton(self)
        self.pushButton_18.setGeometry(QtCore.QRect(kuang_one + 210, kuang_one_y + 18 + 40 + 15, 250, 40))
        self.pushButton_18.setStyleSheet("QPushButton{background-color: #9dc3e6; font-family: 微软雅黑;" +
                                         "border: none;border: 0px solid #9dc3e6;" +
                                         "color: #fff;border-radius: 20px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;padding-left:17px;" +
                                         "display: inline-block;" +
                                         "font-size: 18px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9ad0d0;color: white;"
                                         "}")
        self.pushButton_18.setText("执行")
        self.pushButton_18.clicked.connect(self.on_click_shou)
        self.kuang = QLabel(self)
        self.kuang.setGeometry(QtCore.QRect(kuang_one + 203, kuang_one_y + 18 + 40 + 14, 43, 43))
        self.kuang.setStyleSheet("background-color: white;border-radius: 20px;border: 0px solid #000;")

        self.edit2 = QtWidgets.QLineEdit(self)
        self.edit2.setGeometry(QtCore.QRect(kuang_one + 20, kuang_one_y + 18 + 40 + 15, 220, 40))
        self.edit2.textChanged.connect(self.set_kuaishu)
        self.edit2.setPlaceholderText("内存块数 > 0")
        self.edit2.setStyleSheet("QLineEdit{background-color: #f0f0f0;border-radius: 20px;border:0px solid #f0f0f0;"
                                 "font-size: 18px;font-family: 微软雅黑;padding-left:16px;}")

        self.edit_suiji_num = QtWidgets.QLineEdit(self)
        self.edit_suiji_num.setGeometry(QtCore.QRect(kuang_one + 210, kuang_one_y + 18, 250, 40))
        self.edit_suiji_num.textChanged.connect(self.suiji_num)
        self.edit_suiji_num.setPlaceholderText("随机范围 例如：1 9")
        self.edit_suiji_num.setStyleSheet(
            "QLineEdit{background-color: #f0f0f0;border-radius: 20px;border:0px solid #000;"
            "font-size: 18px;font-family: 微软雅黑;padding-left:44px;}")

        self.yuan3 = QLabel(self)
        self.yuan3.setGeometry(QtCore.QRect(kuang_one + 203, kuang_one_y + 18, 43, 43))
        self.yuan3.setStyleSheet("background-color: white;border-radius: 20px;border: 0px solid #000;")
        self.edit_suiji_size = QtWidgets.QLineEdit(self)
        self.edit_suiji_size.setGeometry(QtCore.QRect(kuang_one + 20, kuang_one_y + 18, 220, 40))
        self.edit_suiji_size.textChanged.connect(self.set_suiji_size)
        self.edit_suiji_size.setPlaceholderText("随机数量 > 0")
        self.edit_suiji_size.setStyleSheet(
            "QLineEdit{background-color: #f0f0f0;border-radius: 20px;border:0px solid #000;"
            "font-size: 18px;font-family: 微软雅黑;padding-left:16px;}")

        self.pushButton_19 = QtWidgets.QPushButton(self)
        self.pushButton_19.setGeometry(QtCore.QRect(kuang_one + 210, kuang_one_y + 18 + 40 + 15, 250, 40))
        self.pushButton_19.setStyleSheet("QPushButton{background-color: #9dc3e6; font-family: 微软雅黑;" +
                                         "border: none;border: 0px solid #9dc3e6;" +
                                         "color: #fff;border-radius: 20px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;padding-left:17px;" +
                                         "display: inline-block;" +
                                         "font-size: 18px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9ad0d0;color: white;"
                                         "}")
        self.pushButton_19.setText("执行")
        self.pushButton_19.clicked.connect(self.on_click_suiji)

        self.yuan2 = QLabel(self)
        self.yuan2.setGeometry(QtCore.QRect(kuang_one + 203, kuang_one_y + 18 + 40 + 14, 43, 43))
        self.yuan2.setStyleSheet("background-color: white;border-radius: 20px;border: 0px solid #000;")
        self.edit22 = QtWidgets.QLineEdit(self)
        self.edit22.setGeometry(QtCore.QRect(kuang_one + 20, kuang_one_y + 18 + 40 + 15, 220, 40))
        self.edit22.textChanged.connect(self.set_neicunkuaishu)
        self.edit22.setPlaceholderText("内存块数 > 0")
        self.edit22.setStyleSheet("QLineEdit{background-color: #f0f0f0;border-radius: 20px;border:0px solid #000;"
                                  "font-size: 18px;font-family: 微软雅黑;padding-left:16px;}")
        self.edit22.hide()
        self.yuan2.hide()
        self.pushButton_19.hide()
        self.edit_suiji_size.hide()
        self.yuan3.hide()
        self.edit_suiji_num.hide()
        self.grid = QGridLayout(self)
        self.grid.setGeometry(QtCore.QRect(500, 300, 330, 50))
        self.color = ["#e89291", "#c4b98b", "#81a8e1", "#8cc9c4", "#83bde2"]
        self.lab_list = []
        self.res = QLabel(self)
        self.res.setScaledContents(True)
        self.res.setStyleSheet("background-color: #f0f0f0;border-radius: 7px;margin:4px;")
        self.res.adjustSize()
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.res)
        self.scroll_area.setStyleSheet("QScrollArea{background-color: #f0f0f0;border: 0px;border-radius: 7px;}" +

                                       "QScrollBar:horizontal {background-color: #bbd7ec;border: 0px;height: 14px;border-radius:7px;}" +
                                       "QScrollBar::handle:horizontal {background-color: #7fa6c8; height: 6px;border-radius:7px;}" +
                                       "QScrollBar::handle:horizontal:hover{background:#7fa6c8;height:6px;border-radius:7px;}" +
                                       "QScrollBar::handle:horizontal:pressed{background-color: #7fa6c8; height:6px;border-radius:7px;}" +
                                       "QScrollBar::add-page{background-color: #bbd7ec;border-radius:7px;}" +
                                       "QScrollBar::sub-page{background-color: #bbd7ec;border-radius:7px;}" +
                                       "QScrollBar::add-line:horizontal{width: 0px;}" +
                                       "QScrollBar::sub-line:horizontal{width: 0px;}" +

                                       "QScrollBar:vertical {background-color: #bbd7ec;border: 0px;width: 14px;border-radius:7px;}" +
                                       "QScrollBar::handle:vertical {background-color: #7fa6c8; width: 6px;border-radius:7px;}" +
                                       "QScrollBar::handle:vertical:hover{background:#7fa6c8;width:6px;border-radius:7px;}" +
                                       "QScrollBar::handle:vertical:pressed{background-color: #7fa6c8; width:6px;border-radius:7px;}" +
                                       "QScrollBar::add-line:vertical{heigth: 0px;border-radius:7px;}" +
                                       "QScrollBar::down-arrow:vertical{heigth: 0px;border-radius:7px;} " +
                                       "QScrollBar::up-arrow:vertical{heigth: 0px;border-radius:7px;}" +
                                       "QScrollBar::sub-line:vertical{heigth: 0px;border-radius:7px;}")
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        # self.v_layout.addWidget(self.scrollbar)
        self.setLayout(self.v_layout)
        self.v_layout.setGeometry(QtCore.QRect(60, 320, 810, 310))
        self.error = QLabel(self)
        self.error.setGeometry(QtCore.QRect(470, 300, 330, 50))
        self.error.setStyleSheet(
            "text-align: center;background-color: #f44336;border-radius: 7px;border: 0px solid #000;color:#fff;font-size:18px;font-family: 微软雅黑;")
        self.errorshadow = QGraphicsDropShadowEffect(self)
        self.errorshadow.setBlurRadius(30)
        cl = QColor("#cacaca")
        self.errorshadow.setColor(cl)
        self.errorshadow.setOffset(0, 0)
        self.error.setText("ERROR:数据不能为空 或 格式错误!!!")
        self.error.setGraphicsEffect(self.errorshadow)
        self.error.setAlignment(Qt.AlignCenter)
        self.error.hide()
        self.pushButton_img = QtWidgets.QPushButton(self)
        self.pushButton_img.setGeometry(QtCore.QRect(self.width() - 175, self.height() - 160, 100, 107))
        self.pushButton_img.setStyleSheet("QPushButton{border-image: url(:/data/mieba.png); font-family: 微软雅黑;" +
                                          "border: none;" +
                                          "color: #fff;border-radius: 7px;" +
                                          "text-align: center;" +
                                          "text-decoration: none;" +
                                          "display: inline-block;" +
                                          "font-size: 19px;" +
                                          "cursor: pointer;}" +
                                          "QPushButton:hover{border-image: url(:/data/ico.png)}")
        self.pushButton_img.clicked.connect(self.on_new_gui)

        self.pushButton_url = QtWidgets.QPushButton(self)
        self.pushButton_url.setGeometry(QtCore.QRect(self.width() - 330, self.height() - 120, 100, 107))
        self.pushButton_url.setStyleSheet("QPushButton{ font-family: 微软雅黑;" +
                                          "border: none;" +
                                          "color: #f7f7f7;border-radius: 7px;" +
                                          "text-align: center;" +
                                          "text-decoration: none;" +
                                          "display: inline-block;" +
                                          "font-size: 30px;" +
                                          "cursor: pointer;}")
        self.pushButton_url.setText("By Pc")
        self.pc_pl = 0
        self.pushButton_url.clicked.connect(self.go_to_url)

        self.queci = QLabel(self)
        self.queci.setGeometry(QtCore.QRect(915, 150, 290, 60))
        self.queci.setStyleSheet("background-color: #f0f0f0;border-radius: 7px;")

        self.queci_text = QtWidgets.QPushButton(self)
        self.queci_text.setGeometry(QtCore.QRect(915, 150, 290, 60))
        self.queci_text.setStyleSheet("QPushButton{ font-family: 微软雅黑;" +
                                      "border: none; " +
                                      "color: #7a7a7a;border-radius: 5px;" +
                                      "text-align: center;" +
                                      "text-decoration: none;" +
                                      "display: inline-block;" +
                                      "font-size: 19px;" +
                                      "cursor: pointer;}")
        self.queci_text.setText("缺页次数")

        self.queci_one = QtWidgets.QPushButton(self)
        self.queci_one.setGeometry(QtCore.QRect(915, 220, 290, 60))
        self.queci_one.setStyleSheet("QPushButton{background-color: white; font-family: 微软雅黑;" +
                                     "border: none; " +
                                     "color: #000;border-radius: 5px;" +
                                     "text-align: center;" +
                                     "text-decoration: none;" +
                                     "display: inline-block;" +
                                     "font-size: 19px;" +
                                     "cursor: pointer;}")

        self.quelv = QLabel(self)
        self.quelv.setGeometry(QtCore.QRect(910, 320, 290, 60))
        self.quelv.setStyleSheet("background-color: #f0f0f0;border-radius: 7px;")

        self.quelv_text = QtWidgets.QPushButton(self)
        self.quelv_text.setGeometry(QtCore.QRect(910, 322, 290, 60))
        self.quelv_text.setStyleSheet("QPushButton{ font-family: 微软雅黑;" +
                                      "border: none; " +
                                      "color: #7a7a7a;border-radius: 5px;" +
                                      "text-align: center;" +
                                      "text-decoration: none;" +
                                      "display: inline-block;" +
                                      "font-size: 19px;" +
                                      "cursor: pointer;}")
        self.quelv_text.setText("缺页率")

        self.quelv_one = QtWidgets.QPushButton(self)
        self.quelv_one.setGeometry(QtCore.QRect(910, 390, 290, 60))
        self.quelv_one.setStyleSheet("QPushButton{background-color: white; font-family: 微软雅黑;" +
                                     "border: none; " +
                                     "color: #000;border-radius: 5px;" +
                                     "text-align: center;" +
                                     "text-decoration: none;" +
                                     "display: inline-block;" +
                                     "font-size: 19px;" +
                                     "cursor: pointer;}")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def go_to_url(self):
        if self.pc_pl == 0:
            self.pushButton_url.setText("By Pl")
            self.pc_pl = 1
        elif self.pc_pl == 1:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://39.97.168.170/'))
            self.pc_pl = 2
        else:
            self.pushButton_url.setText("By Pc")
            self.pc_pl = 0

    def on_new_gui(self):
        self.ex = Example()
        self.ex.show()

    def suiji_num(self, text):
        self.suiji_num = text

    def set_suiji_size(self, text):
        self.suiji_size = text

    def set_neicunkuaishu(self, text):
        self.neicunkuaishu = text

    def setup_yd(self):
        if self.biaotipos == 1:
            self.biaotipos = 2
            self.kuang.hide()
            self.edit2.hide()
            self.pushButton_18.hide()
            self.edit.hide()
            self.edit22.show()
            self.yuan2.show()
            self.pushButton_19.show()
            self.edit_suiji_size.show()
            self.yuan3.show()
            self.edit_suiji_num.show()
            animation = QPropertyAnimation(self)
            animation.setTargetObject(self.biaoti_one)
            animation.setPropertyName(b"pos")
            animation.setStartValue(QPoint(375, 75))
            animation.setEndValue((QPoint(615, 75)))
            animation.setDuration(300)
            animation.start()

    def setup_ydhui(self):
        if self.biaotipos == 2:
            self.biaotipos = 1
            self.edit22.hide()
            self.yuan2.hide()
            self.pushButton_19.hide()
            self.edit_suiji_size.hide()
            self.yuan3.hide()
            self.edit_suiji_num.hide()
            self.kuang.show()
            self.edit2.show()
            self.pushButton_18.show()
            self.edit.show()
            animation = QPropertyAnimation(self)
            animation.setTargetObject(self.biaoti_one)
            animation.setPropertyName(b"pos")
            animation.setStartValue(QPoint(615, 75))
            animation.setEndValue((QPoint(375, 75)))
            animation.setDuration(300)

            animation.start()

    @pyqtSlot()
    def on_click(self):
        self.pushButton_15.setStyleSheet("QPushButton{background-color: #7fa6c8; font-family: 微软雅黑;" +
                                         "border: none;" +
                                         "color: white;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")

        self.pushButton_16.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")

        self.pushButton_17.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")
        self.suanfa = 1

    @pyqtSlot()
    def on_click_two(self):

        self.pushButton_15.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")

        self.pushButton_16.setStyleSheet("QPushButton{background-color: #7fa6c8; font-family: 微软雅黑;" +
                                         "border: none;" +
                                         "color: white;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")

        self.pushButton_17.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")
        self.suanfa = 2

    @pyqtSlot()
    def on_click_three(self):

        self.pushButton_15.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")

        self.pushButton_16.setStyleSheet("QPushButton{background-color: #f0f0f0; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #7a7a7a;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}"
                                         "QPushButton:hover{ "
                                         "    background-color: #9dc3e6;color: white;"
                                         "}")

        self.pushButton_17.setStyleSheet("QPushButton{background-color: #7fa6c8; font-family: 微软雅黑;" +
                                         "border: none;" +
                                         "color: white;border-radius: 7px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        self.suanfa = 3

    @pyqtSlot()
    def setcilv(self, lv, ci):
        self.quelv_one.setText(str("%.4f%%" % (lv * 100)))
        self.queci_one.setText(str(ci) + "次")
        self.labelshadow = QGraphicsDropShadowEffect(self)
        self.labelshadow.setBlurRadius(15)
        cl = QColor("#cacaca")
        self.labelshadow.setColor(cl)
        self.labelshadow.setOffset(1, 1)
        self.queci_one.setGraphicsEffect(self.labelshadow)

        if lv > 0.75:
            self.queci_one.setStyleSheet("QPushButton{background-color: #e89291; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
            self.quelv_one.setStyleSheet("QPushButton{background-color: #e89291; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        elif lv > 0.50:
            self.queci_one.setStyleSheet("QPushButton{background-color: #f1916b; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
            self.quelv_one.setStyleSheet("QPushButton{background-color: #f1916b; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        elif lv > 0.25:
            self.queci_one.setStyleSheet("QPushButton{background-color: #8cc9c4; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
            self.quelv_one.setStyleSheet("QPushButton{background-color: #8cc9c4; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        else:
            self.queci_one.setStyleSheet("QPushButton{background-color:#83bde2; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
            self.quelv_one.setStyleSheet("QPushButton{background-color: #83bde2; font-family: 微软雅黑;" +
                                         "border: none; " +
                                         "color: #fff;border-radius: 5px;" +
                                         "text-align: center;" +
                                         "text-decoration: none;" +
                                         "display: inline-block;" +
                                         "font-size: 19px;" +
                                         "cursor: pointer;}")
        self.labelshadow2 = QGraphicsDropShadowEffect(self)
        self.labelshadow2.setBlurRadius(15)
        cl = QColor("#cacaca")
        self.labelshadow2.setColor(cl)
        self.labelshadow2.setOffset(1, 1)
        self.quelv_one.setGraphicsEffect(self.labelshadow2)

    @pyqtSlot()
    def on_click_suiji(self):

        print("INF-suiji" + str(self.suanfa))

        # 范围
        try:
            if self.suanfa == 1:
                arr_fanwei = str.split(self.suiji_num)
                start = arr_fanwei[0]
                end = arr_fanwei[1]
                size = self.suiji_size
                shu = self.neicunkuaishu
                arr = []
                print(start)
                print(end)
                print(size)
                print(shu)
                for i in range(0, int(size)):
                    arr.append(random.randint(int(start), int(end)))
                print(arr)
                fifo = FIFO.main(arr, int(shu))
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                print("缺页次数===" + str(fifo.get_ci()))
                print("缺页率===" + str(fifo.get_lv()))
                self.setcilv(fifo.get_lv(), fifo.get_ci())
            elif self.suanfa == 2:
                arr_fanwei = str.split(self.suiji_num)
                start = arr_fanwei[0]
                end = arr_fanwei[1]
                size = self.suiji_size
                shu = self.neicunkuaishu
                arr = []
                print(start)
                print(end)
                print(size)
                print(shu)
                for i in range(0, int(size)):
                    arr.append(random.randint(int(start), int(end)))
                print(arr)
                fifo = LRU.main(arr, int(shu))
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                self.setcilv(fifo.get_lv(), fifo.get_ci())
            elif self.suanfa == 3:
                arr_fanwei = str.split(self.suiji_num)
                start = arr_fanwei[0]
                end = arr_fanwei[1]
                size = self.suiji_size
                shu = self.neicunkuaishu
                arr = []
                print(start)
                print(end)
                print(size)
                print(shu)
                for i in range(0, int(size)):
                    arr.append(random.randint(int(start), int(end)))
                print(arr)
                fifo = OPT.OPT(int(shu), arr)
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                self.setcilv(fifo.get_lv(), fifo.get_ci())
        except:
            traceback.print_exc()
            print("ERROR-kong")
            self.error.show()
            self.timer = QTimer()
            self.num = 0
            self.timer.timeout.connect(self.hideerror)
            self.timer.start(1500)

    @pyqtSlot()
    def on_click_shou(self):
        print("INF-self.suanfa=1")
        try:
            if self.suanfa == 1:
                print(self.kuaishu + self.yemian)
                arr_str = str.split(self.yemian)
                arr_int = [int(i) for i in arr_str]
                print(arr_int)
                print("INF==" + str(arr_int) + str(self.kuaishu))
                fifo = FIFO.main(arr_int, int(self.kuaishu))
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                self.setcilv(fifo.get_lv(), fifo.get_ci())

            elif self.suanfa == 2:

                print(self.kuaishu + self.yemian)
                arr_str = str.split(self.yemian)
                arr_int = [int(i) for i in arr_str]
                print(arr_int)
                print("INF==" + str(arr_int) + str(self.kuaishu))
                fifo = LRU.main(arr_int, int(self.kuaishu))
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                self.setcilv(fifo.get_lv(), fifo.get_ci())

            elif self.suanfa == 3:

                print(self.kuaishu + self.yemian)
                arr_str = str.split(self.yemian)
                arr_int = [int(i) for i in arr_str]
                print(arr_int)
                print("INF==" + str(arr_int) + str(self.kuaishu))
                fifo = OPT.OPT(int(self.kuaishu), arr_int)
                res = fifo.get_res()
                print(res)
                self.res.setText(res)
                self.res.adjustSize()
                self.setcilv(fifo.get_lv(), fifo.get_ci())
        except:
            print("ERROR-kong")
            self.error.show()
            self.timer = QTimer()
            self.num = 0
            self.timer.timeout.connect(self.hideerror)
            self.timer.start(1500)

    def hideerror(self):
        self.error.hide()

    def set_kuaishu(self, text):
        self.kuaishu = text

    def set_yemian(self, text):
        self.yemian = text

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")


class MySplash(QWidget):
    def __init__(self):
        super(MySplash, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setObjectName("清华大学得不到的学生")
        self.setWindowTitle("清华大学得不到的学生")
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(1274, 677)
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(15, 15, 1244, 647))
        self.label.setText("")
        palette = QtGui.QPalette()
        self.labelshadow = QGraphicsDropShadowEffect(self)
        self.labelshadow.setBlurRadius(15)
        self.labelshadow.setOffset(1, 1)
        self.label.setGraphicsEffect(self.labelshadow)
        self.label.setScaledContents(True)
        self.pix = QPixmap(":/data/start.png")
        self.label.setPixmap(self.pix)


class LABL(QLabel):
    mylabelSig = pyqtSignal(str)
    mylabelDoubleClickSig = pyqtSignal(str)

    def __int__(self):
        super(LABL, self).__init__()

    def mouseDoubleClickEvent(self, e):
        sigContent = self.objectName()
        self.mylabelDoubleClickSig.emit(sigContent)

    def leaveEvent(self, e):
        jpg = QtGui.QPixmap(":/data/mieba.png")
        self.setPixmap(jpg)

    def enterEvent(self, e):
        jpg = QtGui.QPixmap(":/data/ico.png")
        self.setPixmap(jpg)


def load_Message():
    time.sleep(1)
    qApp.processEvents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = MySplash()
    splash.show()
    qApp.processEvents()
    load_Message()
    splash.close()

    app2 = QtWidgets.QApplication(sys.argv)
    gui = Ui_Form()
    gui.show()

    sys.exit(app2.exec_())
