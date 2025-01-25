import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

class Plotter:

    def __init__(self):
        self.fig = plt.figure()
        self.axes = []
        self.axes.append(self.fig.add_subplot(3, 2, 1))
        self.axes.append(self.fig.add_subplot(3, 2, 2))
        self.axes.append(self.fig.add_subplot(3, 2, 3))
        self.axes.append(self.fig.add_subplot(3, 2, 4))
        self.axes.append(self.fig.add_subplot(3, 2, 5))
        self.axes.append(self.fig.add_subplot(3, 2, 6))
        self.titles = ["Temperature", "Humidity", "Pressure", "Light", "IAQ Score", "CO2"]

        self.graph_data = [{}, {}, {}, {}, {}, {}]

        self.ani = animation.FuncAnimation(self.fig, self.animate, interval = 1000)
        plt.ion()
        plt.show()

    def add_data(self, id, index, time, data):
        if not id in self.graph_data[index]:
            self.graph_data[index][id] = []
        self.graph_data[index][id].append((time, data))

    def amount_of_data(self):
        return len(self.graph_data)

    def clear(self):
        for axis in self.axes:
            axis.clear()

    def add_titles(self):
        for i in range(len(self.axes)):
            self.axes[i].title.set_text(self.titles[i])

    def animate_graph(self, index):
        axis = self.axes[index]
        data = self.graph_data[index]

        for id, values in data.items():
            x = []
            y = []
            for point in values:
                x.append(point[0])
                y.append(point[1])
            axis.plot(x, y, label = id)

    def animate(self, i):
        self.clear()
        self.add_titles()
        for index in range(6):
            self.animate_graph(index)

    def GUI_update(self):
        plt.pause(0.001)