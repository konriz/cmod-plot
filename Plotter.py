import math

import plotly.plotly as py
from plotly.graph_objs import *


def plot(data):
    # TODO create Scatters from data_set and append them to curves array -> plot curve

    curves = []
    curve = Scatter(x=data[0], y=data[1])
    curves.append(curve)
    plot_data = Data(curves)

    x_axis_template = dict(
        title="CMOD [mm]",
        zeroline=True,
        showline=True,
        dtick=0.5,
        range=[0, 5])
    y_axis_template = dict(
        title="Force [kN]",
        zeroline=True,
        showline=True,
        range=[0, math.ceil(max(data[1]) + 1)])

    layout = Layout(xaxis=x_axis_template, yaxis=y_axis_template)

    fig = Figure(data=plot_data, layout=layout)
    py.plot(fig)

