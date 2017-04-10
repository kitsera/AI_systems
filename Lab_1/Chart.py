import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets


class Chart(FigureCanvas):

    def __init__(self,parent=None, width=32, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def draw_chart(self, field):
        self.axes.clear()
        colors = ['ro', 'bo', 'ko', 'go', 'mo', 'co', 'yo']
        center_colors = ['r^', 'b^', 'k^', 'g^', 'm^', 'c^', 'y^']
        i = 0

        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        for cluster in field.get_clusters():
            x_array = []
            y_array = []
            for point in cluster.get_points():
                x = point.get_x()
                y = point.get_y()
                x_array.append(x)
                y_array.append(y)
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x

                if y < min_y:
                    min_y = y
                elif y > max_y:
                    max_y = y
            self.axes.plot(x_array, y_array, colors[i], label = 'cluster ' + str(i+1) + ' points')
            self.axes.plot(cluster.get_center().get_x(), cluster.get_center().get_y(), center_colors[i], label = 'cluster ' + str(i+1) + ' center')
            self.axes.legend()
            i += 1

        self.axes.set_ylim(min_y-1, max_y+1)
        self.axes.set_xlim(min_x-1, max_x+1)
        self.draw()