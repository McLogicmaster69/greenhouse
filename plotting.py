import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

class Plotter:
    """
    GUI for plotting graphs to do with sensor data
    """
    def __init__(self) -> None:
        """
        Creates a figure and puts 6 graphs on it for different data
        """
        # Create figure
        self.fig = plt.figure()

        # Create graphs on figure
        self.axes = []
        self.axes.append(self.fig.add_subplot(3, 2, 1))
        self.axes.append(self.fig.add_subplot(3, 2, 2))
        self.axes.append(self.fig.add_subplot(3, 2, 3))
        self.axes.append(self.fig.add_subplot(3, 2, 4))
        self.axes.append(self.fig.add_subplot(3, 2, 5))
        self.axes.append(self.fig.add_subplot(3, 2, 6))
        self.TITLES = ["Temperature", "Humidity", "Pressure", "Light", "IAQ Score", "CO2"]
        self.graph_data = [{}, {}, {}, {}, {}, {}]

        # Start animation loop to constantly update graphs with new data
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval = 1000)

        # Show graph
        plt.ion()
        plt.show()

    def add_data(self, id, index : int, time, data) -> None:
        """
        Add data to the graphs
        """
        if not id in self.graph_data[index]:
            self.graph_data[index][id] = []
        self.graph_data[index][id].append((time, data))

    def clear(self) -> None:
        """
        Clears the data displayed on the graphs
        """
        for axis in self.axes:
            axis.clear()

    def add_titles(self) -> None:
        """
        Adds the titles to each graph
        """
        for i in range(len(self.axes)):
            self.axes[i].title.set_text(self.TITLES[i])

    def animate_graph(self, index) -> None:
        """
        Updates the visuals of a graph with the data stored for it
        """
        axis = self.axes[index]
        data = self.graph_data[index]
        for id, values in data.items():
            x = []
            y = []
            for point in values:
                x.append(point[0])
                y.append(point[1])
            axis.plot(x, y, label = id)

    def animate(self, i) -> None:
        """
        Update the visuals of all graphs
        """
        self.clear()
        self.add_titles()
        for index in range(6):
            self.animate_graph(index)

    def GUI_update(self) -> None:
        """
        Allows time for the GUI to update
        """
        plt.pause(0.001)