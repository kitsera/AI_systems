import sys

import ISODATA
from PyQt5 import QtWidgets, QtGui, QtCore
from Utils import *

from Lab_1.Chart import Chart


class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.set_ui()

    def set_ui(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        points = [Point.Point(-4, 0), Point.Point(-4, -1), Point.Point(-8, -5), Point.Point(-9, -5),
                  Point.Point(-8, -6), Point.Point(-7, -6), Point.Point(3, 0), Point.Point(2, -1),
                  Point.Point(1, -1), Point.Point(1, -2), Point.Point(-2, 6), Point.Point(-2, -7), Point.Point(0, -7)]

        f_h_l = QtWidgets.QHBoxLayout()
        k_l = QtWidgets.QLabel("K")
        k_l.setFixedWidth(20)
        self.k_edit = QtWidgets.QLineEdit("4")

        Qn_l = QtWidgets.QLabel("Qn")
        Qn_l.setFixedWidth(20)
        self.Qn_edit = QtWidgets.QLineEdit('1')

        s_h_l = QtWidgets.QHBoxLayout()
        Qs_l = QtWidgets.QLabel("Qs")
        Qs_l.setFixedWidth(20)
        self.Qs_edit = QtWidgets.QLineEdit('1')

        Qc_l = QtWidgets.QLabel("Qc")
        Qc_l.setFixedWidth(20)
        self.Qc_edit = QtWidgets.QLineEdit('3')

        t_h_l = QtWidgets.QHBoxLayout()
        l_l = QtWidgets.QLabel("L")
        l_l.setFixedWidth(20)
        self.l_edit = QtWidgets.QLineEdit('1')

        i_l = QtWidgets.QLabel("I")
        i_l.setFixedWidth(20)
        self.i_edit = QtWidgets.QLineEdit('4')

        f_h_l.addWidget(k_l)
        f_h_l.addWidget(self.k_edit)
        f_h_l.addWidget(Qn_l)
        f_h_l.addWidget(self.Qn_edit)

        s_h_l.addWidget(Qs_l)
        s_h_l.addWidget(self.Qs_edit)
        s_h_l.addWidget(Qc_l)
        s_h_l.addWidget(self.Qc_edit)

        t_h_l.addWidget(l_l)
        t_h_l.addWidget(self.l_edit)
        t_h_l.addWidget(i_l)
        t_h_l.addWidget(self.i_edit)


        self.chart = Chart()

        num_label = QtWidgets.QLabel("№")
        x_label = QtWidgets.QLabel("X")
        y_label = QtWidgets.QLabel("Y")
        num_label.setFixedHeight(10)
        x_label.setFixedHeight(10)
        y_label.setFixedHeight(10)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(num_label)
        h_layout.addWidget(x_label)
        h_layout.addWidget(y_label)
        point_label = []
        self.x_edit = []
        self.y_edit = []
        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addLayout(f_h_l)
        v_layout.addLayout(s_h_l)
        v_layout.addLayout(t_h_l)
        v_layout.addLayout(h_layout)
        for i in range(13):
            h_layout = QtWidgets.QHBoxLayout()
            point_label.append(QtWidgets.QLabel(str(i+1)))
            point_label[i].setFixedWidth(17)
            point_label[i].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
            self.x_edit.append(QtWidgets.QLineEdit(str(points[i].get_x())))
            self.y_edit.append(QtWidgets.QLineEdit(str(points[i].get_y())))
            h_layout.addWidget(point_label[i])
            h_layout.addWidget(self.x_edit[i])
            h_layout.addWidget(self.y_edit[i])
            v_layout.addLayout(h_layout)
            self.x_edit[i].setValidator(QtGui.QDoubleValidator(-10, 20, 1))
            self.y_edit[i].setValidator(QtGui.QDoubleValidator(-10, 20, 1))
        btn = QtWidgets.QPushButton("Кластеризувати")
        v_layout.addWidget(btn)
        main_layout.addLayout(v_layout)
        main_layout.addWidget(self.chart)
        btn.pressed.connect(self.calc_clusters)

    def calc_clusters(self):
        k = int(self.k_edit.text())
        Qn = int(self.Qn_edit.text())
        Qs = int(self.Qs_edit.text())
        Qc = int(self.Qc_edit.text())
        i = int(self.i_edit.text())
        l = int(self.l_edit.text())
        points = []
        for j in range(len(self.x_edit)):
            points.append(Point.Point(int(self.x_edit[j].text()), int(self.y_edit[j].text())))
        print(points)
        data = ISODATA.ISODATA(points, i, k, Qn, Qs, Qc, l)
        data.print_field()
        field = data.get_field()
        self.chart.draw_chart(field)






if __name__ == '__main__':
    qApp = QtWidgets.QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.setWindowTitle("ISO DATA")
    aw.show()

    points = [Point.Point(-4, 0), Point.Point(-4, -1), Point.Point(-8, -5), Point.Point(-9, -5),
              Point.Point(-8, -6), Point.Point(-7, -6), Point.Point(3, 0), Point.Point(2, -1),
              Point.Point(1, -1), Point.Point(1, -2), Point.Point(-2, 6), Point.Point(-2, -7), Point.Point(0, -7)]

    sys.exit(qApp.exec_())