import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

class Plotter:

    def __init__(self):
        self.fig = plt.figure()
        self.axes = []
        self.axes.append(self.fig.add_subplot(2, 2, 1))
        self.axes.append(self.fig.add_subplot(2, 2, 2))
        self.axes.append(self.fig.add_subplot(2, 2, 3))
        self.axes.append(self.fig.add_subplot(2, 2, 4))
        self.titles = ["Graph A", "Graph B", "Graph C", "Graph D"]
        self.graph_data = []

        self.ani = animation.FuncAnimation(self.fig, self.animate, interval = 1000)
        plt.ion()
        plt.show(block = False)

    def add_data(self, data):
        self.graph_data.append(data)

    def pop_data(self):
        if len(self.graph_data) > 0:
            del self.graph_data[0]

    def amount_of_data(self):
        return len(self.graph_data)

    def clear(self):
        for axis in self.axes:
            axis.clear()

    def add_titles(self):
        for i in range(len(self.axes)):
            self.axes[i].title.set_text(self.titles[i])

    def animate(self, i):
        xs = []
        data = []

        for i in range(len(self.axes)):
            data.append([])

        for d in self.graph_data:
            xs.append(d[0])
            for i in range(len(self.axes)):
                data[i].append(d[i + 1])

        self.clear()
        self.add_titles()

        for i in range(len(self.axes)):
            self.axes[i].plot(xs, data[i])

    def GUI_update(self):
        plt.pause(0.01)