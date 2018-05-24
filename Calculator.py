from SadFile import *
from CmodData import *
import plotly.plotly as py
from plotly.graph_objs import *


def calculate_cmod(file_name):
    file = SadFile(file_name)
    data = CmodData(file.values)

    results = "LOP = {1}\n" \
              "CMOD1 = {0[0]}\n" \
              "CMOD2 = {0[1]}\n" \
              "CMOD3 = {0[2]}\n" \
              "CMOD4 = {0[3]}\n".format(data.cmod_force, data.lop)

    output_file = open(file.output_dir + file.name + "_result.asc", "w+")
    output_file.write(results)
    output_file.close()
    print(file.name + " calculated\n")

    return data


def plot_cmod(file_name):

    data = calculate_cmod(file_name)
    curve = Scatter(x=data.total_cmod, y=data.total_force)
    plot_data = Data([curve])

    x_axis_template = dict(
        title="CMOD [mm]",
        zeroline=True,
        showline=True,
        dtick=0.5,
        range=5)
    y_axis_template = dict(
        title="Force [kN]",
        zeroline=True,
        showline=True)

    layout = Layout(xaxis=x_axis_template, yaxis=y_axis_template)

    fig = Figure(data=plot_data,  layout=layout)
    plot_name = py.plot(fig, filename=file_name)
