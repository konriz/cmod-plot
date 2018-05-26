import plotly.plotly as py
from plotly.graph_objs import *


def plot(curve_set):
    # TODO create Scatters from data_set and append them to curves array -> plot curve

    curves = []
    for data in curve_set:
        curve = Scatter(x=data[0], y=data[1], name=data[2])
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
        range=[0, 40]
        )

    layout = Layout(xaxis=x_axis_template, yaxis=y_axis_template)

    fig = Figure(data=plot_data, layout=layout)
    py.plot(fig)

