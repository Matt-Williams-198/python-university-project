import numpy as np
import matplotlib.pyplot as plt


class ExponentAX:
    """
    ExponentAX is a class which contains instance variables for coefficients and storage of data points.
    It also contains functions for generating the y-axis and x-axis, there is also a function for plotting the data
    points


    ----

    Functions:

    __init__ -- constructor(creates the instance variables)

    ----

    Methods:

    fx -- creates a list of data points along the function at a resolution of 1 units

    plotfx -- plots a graph of the exponent
    """
    def __init__(self, a: float):
        """Constructor for ExponentAX. It has instance variables for the constant "a",
        the list of the data points for the y-axis and a list for the x-axis data points

        :param a: constant for the equation exp(ax)"""

        self.a = a  # constant in equation exp(ax)
        self.y_axis = []  # list of data points for the x-axis
        self.x_axis = []  # list of data points for the y-axis

    def fx(self):
        """This method generates the data points for the x-axis and y-axis in accordance
        with the exponential function using numpy's exponential funtion. Iterating through
        100 data points, calculating the corresponding y-axis data points for each value on
        the x-axis
        """
        for i in range(100):  # increments through a range of 0 to 100 to create data points along the x and y-axis
            self.y_axis.append(np.exp(self.a * i))  # calculates data points for the y-axis and stores them
            self.x_axis.append(i)  # stores the increment which is also the x-axis data point at each iteration

    def plotfx(self):
        """This method plots the data points which have been previously calculated using
        and labels the axis for the graph.
        """
        plt.plot(self.x_axis, self.y_axis, color="red")  # plots the data points and states graph line colour
        plt.title(f"Exponent({self.a}x)")  # gives the plot a title using
        plt.xlabel("x")  # labels the x-axis
        plt.ylabel("exp(ax)")  # labels the y-axis
        plt.show()  # shows the plot

    def mainloop(self):
        """This function acts to call all functions within the class to generate the data points
        and then plot the points with labelled axis"""
        self.fx()  # runs the instance method fx
        self.plotfx()  # runs instance method plotfx
