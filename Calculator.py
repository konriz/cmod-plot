from SadFile import *
from CmodData import *
import Plotter


def report(data_set):
    """prints reports for data set"""
    for data in data_set:
        data.report()


def multi_plot(data_set):
    """plots one plot for multiple curves"""
    Plotter.plot(extract_curves(data_set))


def plot(data_set):
    """plots one plot per curve"""
    for curve in extract_curves(data_set):
        Plotter.plot([curve])


def create_data_set(names):
    """creates data set from multiple files"""
    data_set = []
    for name in names:
        data = CmodData()
        data.analyse(SadFile(name))
        data_set.append(data)
    return data_set


def extract_curves(data_set):
    curves = []
    for data in data_set:
        curves.append(data.extract_curve())
    return curves


def average_curves(data_set):
    """creates averaged curve from data set"""
    x_points = []
    for i in range(0, 1000):
        x_points.append(i/1000)

    for i in range(101, 500):
        x_points.append(i / 100)

    y_points = []

    for x_point in x_points:
        y_point = 0.0
        for data in data_set:
            y_point += data.find_force(x_point)[1]
        y_points.append(y_point / 3.0)

    average_curve = [x_points, y_points, "average"]

    return average_curve
