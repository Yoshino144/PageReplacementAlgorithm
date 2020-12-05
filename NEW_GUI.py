# coding=utf-8
import random
import sys
import time
import traceback

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtChart import QLineSeries, QValueAxis, QChartView, QSplineSeries, QChart
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QPoint, QTimer, QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QColor, QBrush, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import LRU
import FIFO
import OPT


class Example(QMainWindow):

    def __init__(self, ):
        super().__init__()
        self.bijiao = [0, 0, 0]

        self.res = ""
        self.queue = []
        self.k = -1
        self.flag = -1

        try:
            self.initUI()
            self.chart_init(10)
        except:
            traceback.print_exc()

    def initUI(self):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Sysytem\\Desktop\\zhong\\data\\ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.resize(1000, 700)
        self.setWindowTitle('Icon')

        self.setObjectName("清华大学得不到的学生")
        self.setWindowTitle("一枚小乖乖~")
        self.label = QLabel(self)
        self.label.setWindowTitle("清华大学得不到的学生")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setGeometry(QtCore.QRect(15, 15, 970, self.height() - 30))
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
        self.pushButton_12.clicked.connect(self.close)

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

        self.color = ["#e89291", "#c4b98b", "#81a8e1", "#8cc9c4", "#83bde2"]
        # -----------------------------------------------------------------测试数量------------------------
        error = QtWidgets.QLineEdit(self)
        error.setGeometry(QtCore.QRect(70, 70, 150, 50))
        error.setStyleSheet("text-align: center;background-color: " + self.color[
            0] + ";border-radius: 7px;border: 0px solid #000;color:#ffffff;font-size:20px;font-family: 微软雅黑;")
        errorshadow = QGraphicsDropShadowEffect(self)
        error.setPlaceholderText("测试数量")
        errorshadow.setBlurRadius(30)
        cl = QColor("#cacaca")
        errorshadow.setColor(cl)
        error.setAlignment(Qt.AlignCenter)
        errorshadow.setOffset(0, 0)
        error.textChanged.connect(self.set_suliang)
        # error.setGraphicsEffect(errorshadow)

        # -----------------------------------------------------------------随机范围------------------------

        fan = QtWidgets.QLineEdit(self)
        fan.setGeometry(QtCore.QRect(240, 70, 150, 50))
        fan.setStyleSheet("text-align: center;background-color: " + self.color[
            2] + ";border-radius: 7px;border: 0px solid #000;color:#ffffff;font-size:20px;font-family: 微软雅黑;")
        fanshadow = QGraphicsDropShadowEffect(self)
        fanshadow.setBlurRadius(30)
        fancl = QColor("#cacaca")
        fan.setPlaceholderText("随机范围")
        fanshadow.setColor(fancl)
        fan.setAlignment(Qt.AlignCenter)
        fanshadow.setOffset(0, 0)
        fan.textChanged.connect(self.set_fanwei)
        # fan.setGraphicsEffect(fanshadow)

        # -----------------------------------------------------------------内存块数-----------------------

        kuai = QtWidgets.QLineEdit(self)
        kuai.setGeometry(QtCore.QRect(410, 70, 150, 50))
        kuai.setStyleSheet("text-align: center;background-color: " + self.color[
            3] + ";border-radius: 7px;border: 0px solid #000;color:#ffffff;font-size:20px;font-family: 微软雅黑;")
        kuaishadow = QGraphicsDropShadowEffect(self)
        kuaishadow.setBlurRadius(30)
        kuaicl = QColor("#cacaca")
        kuai.setPlaceholderText("内存块数")
        kuaishadow.setColor(kuaicl)
        kuai.setAlignment(Qt.AlignCenter)
        kuaishadow.setOffset(0, 0)
        kuai.textChanged.connect(self.set_kuai)
        # kuai.setGraphicsEffect(kuaishadow)

        self.Button = QtWidgets.QPushButton(self)
        self.Button.setGeometry(QtCore.QRect(580, 70, 150, 50))
        self.Button.setStyleSheet("QPushButton{text-align: center;background-color: #83bde2;"
                                  "border-radius: 7px;border: 0px solid #000;color:#ffffff;"
                                  "font-size:20px;font-family: 微软雅黑;}" +
                                  "QPushButton:hover{ " +
                                  "    background-color: #9ad0d0;color: white;" +
                                  "}")
        Buttonshadow = QGraphicsDropShadowEffect(self)
        Buttonshadow.setBlurRadius(30)
        Buttoncl = QColor("#cacaca")
        self.Button.setText("执行")
        Buttonshadow.setColor(Buttoncl)
        Buttonshadow.setOffset(0, 0)
        # Button.setGraphicsEffect(Buttonshadow)
        self.Button.clicked.connect(self.on_click_start)

        self.avgflag = 0

        self.qq = QtWidgets.QPushButton(self)
        self.qq.setGeometry(QtCore.QRect(750, 70, 180, 50))
        self.qq.setStyleSheet(
            "color: #000;text-align: center;background-color: #f0f0f0;border-radius: 7px;border: 0px solid #000;font-size:14px;font-family: 微软雅黑;")
        self.qq.clicked.connect(self.on_avg)

        self.show()

    def on_avg(self):
        if self.avgflag == 0:
            self.series.hide()

            self.serieslru.hide()

            self.seriesopt.hide()

            self.seriesfifoavg.show()

            self.serieslruavg.show()

            self.seriesoptavg.show()
            self.avgflag = 1
        else:

            self.series.show()

            self.serieslru.show()

            self.seriesopt.show()

            self.seriesfifoavg.hide()

            self.serieslruavg.hide()

            self.seriesoptavg.hide()
            self.avgflag = 0

    def set_kuai(self, text):
        self.kuai = text

    def set_fanwei(self, text):
        self.fan = text

    def set_suliang(self, text):
        self.su = text

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

    def on_click_start(self):
        try:
            self.jishu = 0
            self.thread = MyThread()
            self.thread.set_su(self.su)
            self.thread.set_kuai(self.kuai)
            self.thread.set_x(self.dtaxisX)
            self.thread.set_fan(self.fan)
            self.thread.det_bijiao(self.bijiao)
            self.dailist = []
            self.avg = []
            self.avg1 = []
            self.avg2 = []
            self.dailistlru = []
            self.dailistopt = []
            self.thread.sinOut.connect(self.change)
            self.thread.start()

            # self.qq.setText("FIFO:%0.2f   LRU:%0.2f \n OPT:%0.2f" % (self.bijiao[0], self.bijiao[1], self.bijiao[2]))



        except:
            traceback.print_exc()
        # self.sinOut.emit(self.dailist)
        # self.sinOut2.emit(self.dailistlru)
        # self.sinOut3.emit(self.dailistopt)

    def change(self, dailist):
        try:
            # print(dailist)
            # arr = str.split(dailist)
            # print(arr)

            flag = 0
            start = 0
            flag = dailist.find(" ", flag)
            flag = dailist.find(" ", flag + 1)
            end = flag
            arr = str.split(dailist[start:end])

            start = flag
            flag = dailist.find(" ", flag + 1)
            flag = dailist.find(" ", flag + 1)
            end = flag
            arr1 = str.split(dailist[start:end])

            start = flag
            flag = dailist.find(" ", flag + 1)
            flag = dailist.find(" ", flag + 1)
            end = flag
            arr2 = str.split(dailist[start:end])

            self.dailist.append(QPointF(float(arr[0]), float(arr[1])))

            self.dailistlru.append(QPointF(float(arr1[0]), float(arr1[1])))

            self.dailistopt.append(QPointF(float(arr2[0]), float(arr2[1])))
            #
            self.series.replace(self.dailist)
            self.serieslru.replace(self.dailistlru)
            self.seriesopt.replace(self.dailistopt)

            if self.jishu == 0:
                self.bijiao[0] = float(arr[1])
                self.bijiao[1] = float(arr1[1])
                self.bijiao[2] = float(arr2[1])
                self.jishu = 1
            else:
                self.bijiao[0] = (float(arr[1]) + self.bijiao[0]) / 2.0
                self.bijiao[1] = (float(arr1[1]) + self.bijiao[1]) / 2.0
                self.bijiao[2] = (float(arr2[1]) + self.bijiao[2]) / 2.0
                self.jishu = self.jishu + 1

            self.avg.append(QPointF(float(arr[0]), self.bijiao[0]))
            self.avg1.append(QPointF(float(arr[0]), self.bijiao[1]))
            self.avg2.append(QPointF(float(arr[0]), self.bijiao[2]))

            # print(self.avg)
            self.seriesfifoavg.replace(self.avg)
            self.serieslruavg.replace(self.avg1)
            self.seriesoptavg.replace(self.avg2)

            self.qq.setText("FIFO:%0.2f   LRU:%0.2f \n OPT:%0.2f" % (self.bijiao[0], self.bijiao[1], self.bijiao[2]))
        except:
            traceback.print_exc()

    def drawLine(self):
        self.series.replace(self.dailist)
        # print("uiy")

    def chart_init(self, su):
        self.start_num = 0
        self.chart = QChartView(self)
        self.chart.setGeometry(50, 150, self.width() - 100, self.height() - 150 - 50)  # 设置charView位置、大小
        self.series = QSplineSeries()
        self.series.setName("FIFO")
        self.chart.chart().addSeries(self.series)

        pen = QPen(Qt.gray)
        pen.setWidth(2)
        self.serieslru = QSplineSeries()
        self.serieslru.setPen(pen)
        self.serieslru.setName("LRU")
        self.serieslru.setColor(QColor("#e89291"))
        self.chart.chart().addSeries(self.serieslru)

        pen2 = QPen(Qt.gray)
        pen2.setWidth(2)
        self.seriesopt = QSplineSeries()
        self.seriesopt.setPen(pen2)
        self.seriesopt.setColor(QColor("#3ea54f"))
        self.seriesopt.setName("OPT")
        self.chart.chart().addSeries(self.seriesopt)

        penfifo = QPen(Qt.gray)
        penfifo.setWidth(2)
        self.seriesfifoavg = QSplineSeries()
        self.seriesfifoavg.setPen(penfifo)
        self.seriesfifoavg.setName("FIFO-avg")
        self.seriesfifoavg.setColor(QColor("#209fdf"))
        self.chart.chart().addSeries(self.seriesfifoavg)
        self.seriesfifoavg.hide()

        penavg = QPen(Qt.gray)
        penavg.setWidth(2)
        self.serieslruavg = QSplineSeries()
        self.serieslruavg.setPen(penavg)
        self.serieslruavg.setName("LRU-avg")
        self.serieslruavg.setColor(QColor("#e89291"))
        self.chart.chart().addSeries(self.serieslruavg)
        self.serieslruavg.hide()

        pen2avg = QPen(Qt.gray)
        pen2avg.setWidth(2)
        self.seriesoptavg = QSplineSeries()
        self.seriesoptavg.setPen(pen2avg)
        self.seriesoptavg.setColor(QColor("#3ea54f"))
        self.seriesoptavg.setName("OPT-avg")
        self.chart.chart().addSeries(self.seriesoptavg)
        self.seriesoptavg.hide()

        self.dtaxisX = QValueAxis()
        self.vlaxisY = QValueAxis()
        self.dtaxisX.setMin(10)
        self.dtaxisX.setMax(100)
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(100)
        self.dtaxisX.setTickCount(6)
        self.vlaxisY.setTickCount(11)
        self.dtaxisX.setTitleText("页数")
        self.vlaxisY.setTitleText("缺页率")
        self.vlaxisY.setGridLineVisible(False)
        self.chart.chart().addAxis(self.dtaxisX, Qt.AlignBottom)
        self.chart.chart().addAxis(self.vlaxisY, Qt.AlignLeft)
        self.series.attachAxis(self.dtaxisX)
        self.series.attachAxis(self.vlaxisY)

        self.serieslru.attachAxis(self.dtaxisX)
        self.serieslru.attachAxis(self.vlaxisY)

        self.seriesopt.attachAxis(self.dtaxisX)
        self.seriesopt.attachAxis(self.vlaxisY)

        self.seriesoptavg.attachAxis(self.dtaxisX)
        self.seriesoptavg.attachAxis(self.vlaxisY)
        self.serieslruavg.attachAxis(self.dtaxisX)
        self.serieslruavg.attachAxis(self.vlaxisY)
        self.seriesfifoavg.attachAxis(self.dtaxisX)
        self.seriesfifoavg.attachAxis(self.vlaxisY)

        self.chart.chart().setTitleBrush(QBrush(Qt.cyan))
        cc = QColor("#f0f0f0")
        self.chart.setBackgroundBrush(cc)
        self.chart.setStyleSheet("QChartView{ background-color: #83bde2;border-radius: 20px;}")
        self.chart.show()


class MyThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def set_su(self, su):
        self.su = su

    def set_kuai(self, kuai):
        self.kuai = kuai

    def set_x(self, dtaxisX):
        self.dtaxisX = dtaxisX

    def set_fan(self, fan):
        self.fan = fan

    def det_bijiao(self, bijiao):
        self.bijiao = bijiao

    def det_dailist(self, dailist):
        self.dailist = dailist

    def det_dailistlru(self, dailistlru):
        self.dailistlru = dailistlru

    def det_dailistopt(self, dailistopt):
        self.dailistopt = dailistopt

    def run(self):
        self.cwl = 0.0
        self.dailist = []
        self.dailistlru = []
        self.dailistopt = []
        # print("start")
        try:

            # self.timer = QTimer(self)
            # self.timer.timeout.connect(self.drawLine)
            # self.timer.start(1)
            self.start_num = 10
            shuliang = self.su
            self.dtaxisX.setMax(int(shuliang) + self.start_num)
            kuaishu = self.kuai

            arr_fanwei = str.split(self.fan)
            start = arr_fanwei[0]
            end = arr_fanwei[1]
            for i in range(3, int(shuliang) + self.start_num):
                arr = []
                for arr_p in range(0, i):
                    arr.append(random.randint(int(start), int(end)))
                # print(arr)

                self.fifo = FIFO.main(arr, int(kuaishu))
                # print("错误率fifo" + str(i) + ":" + str(self.fifo.get_lv()))
                self.cwl = self.fifo.get_lv()
                #
                # self.dailist.append(QPointF(self.start_num, self.fifo.get_lv() * 100))

                self.lru = LRU.main(arr, int(kuaishu))
                # print("错误率lru" + str(i) + ":" + str(self.lru.get_lv()))
                # self.dailistlru.append(QPointF(self.start_num, self.lru.get_lv() * 100))

                self.opt = OPT.OPT(int(kuaishu), arr)
                # print("错误率opt" + str(i) + ":" + str(self.opt.get_lv()))
                # self.dailistopt.append(QPointF(self.start_num, self.opt.get_lv() * 100))

                # self.dailist.append(QPointF(i/100, i/100))
                self.start_num = self.start_num + 1

                # self.series.replace(self.dailist)
                # self.serieslru.replace(self.dailistlru)
                # self.seriesopt.replace(self.dailistopt)

                # self.sinOut.emit("[[" + str(self.start_num) + "," + str(self.fifo.get_lv() * 100) + "]," +
                #                  "[ " + str(self.start_num) + "," + str(self.lru.get_lv() * 100) + "]," +
                #                  "[ " + str(self.start_num) + "," + str(self.opt.get_lv() * 100) + " ]]")

                self.sinOut.emit("%d %0.2f %d %0.2f %d %0.2f" % (
                self.start_num, self.fifo.get_lv() * 100, self.start_num, self.lru.get_lv() * 100, self.start_num,
                self.opt.get_lv() * 100))

                # if self.fifo.get_lv()>self.lru.get_lv() and self.fifo.get_lv() >self.opt.get_lv()  :
                #     self.bijiao[0] = self.bijiao[0]+1
                # elif self.lru.get_lv()>self.fifo.get_lv() and self.lru.get_lv() >self.opt.get_lv():
                #     self.bijiao[1] = self.bijiao[1]+1
                # elif self.opt.get_lv()>self.fifo.get_lv() and self.opt.get_lv()>self.lru.get_lv():
                #     self.bijiao[2] = self.bijiao[2]+1

            #     if i == 3:
            #         self.bijiao[0] = self.fifo.get_lv()
            #         self.bijiao[1] = self.lru.get_lv()
            #         self.bijiao[2] = self.opt.get_lv()
            #     else:
            #         self.bijiao[0] = (self.fifo.get_lv() + self.bijiao[0]) / 2.0
            #         self.bijiao[1] = (self.lru.get_lv() + self.bijiao[1]) / 2.0
            #         self.bijiao[2] = (self.opt.get_lv() + self.bijiao[2]) / 2.0
            #
            # # self.qq.setText("FIFO:%0.2f   LRU:%0.2f \n OPT:%0.2f" % (self.bijiao[0], self.bijiao[1], self.bijiao[2]))
            # point_6 = QPointF(1.00, 0.5)
            # point_7 = QPointF(2.00, 0.6)
            # point_8 = QPointF(3.00, 0.8)
            # self._1_point_list.append(point_6)
            # self._1_point_list.append(point_7)
            # self._1_point_list.append(point_8)
            # self.series_1.append(self._1_point_list)
        except:
            traceback.print_exc()
