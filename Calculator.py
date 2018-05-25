from SadFile import *
from CmodData import *


def report(names):
    for name in names:
        data = CmodData()
        data.analyse(SadFile(name))
        data.report()


def plot(names):
    for name in names:
        data = CmodData()
        data.analyse(SadFile(name))
        data.plot()
