import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from FileLoader import FileLoader
import seaborn as sns


def wrong_params(data, features):
    try:
        if not isinstance(features, list):
            raise TypeError("Error : Features must be a list")
        for var in features:
            tmp = data[var]
            if not isinstance(tmp.min(), (float, int)):
                raise TypeError("Error : Features \"{}\" is not numerical"
                                .format(var))
        return 0
    except Exception as msg:
        if type(msg) == KeyError:
            print("Key Error: {} is not a valid Dataframe column".format(msg))
        else:
            print(msg)
        return 1


class MyPlotLib:

    def __init__(self):
        pass

    def histogram(self, data, features):
        if wrong_params(data, features):
            return 1
        for var in features:
            data_var = data[['ID', var]].drop_duplicates().dropna()
            data_var = data_var[var]
            plt.hist(data_var,
                     range=[data_var.min(), data_var.max()],
                     edgecolor='black')
            plt.xlabel(var)
            plt.ylabel("Occurence")
            plt.show()
        return 0

    def density(self, data, features):
        if wrong_params(data, features):
            return 1
        for var in features:
            data_var = data[['ID', var]].drop_duplicates().dropna()
            data_var = data_var[var]
            sns.kdeplot(data_var, label=var)
        plt.xlabel(None)
        plt.legend()
        plt.show()
        return 0

    def pair_plot(self, data, features):
        if wrong_params(data, features):
            return 1
        # seaborn
        sns.pairplot(data[features])
        """
        # matplotlib
        to_plot = data[features]
        to_plot.plot.scatter(features[0], features[1])
        to_plot.plot.scatter(features[1], features[0])
        """
        plt.show()

    def box_plot(self, data, features):
        if wrong_params(data, features):
            return 1
        to_plot = data[features]
        to_plot.boxplot()
        plt.show()


if len(sys.argv) != 1:
    sys.exit("Usage : python3 <exec_file>")
loader = FileLoader()
data = loader.load("athlete_events.csv")
myplot = MyPlotLib()
myplot.histogram(data, ['Weight', 'Height'])
myplot.density(data, ['Weight', 'Height'])
myplot.pair_plot(data, ['Weight', 'Height'])
myplot.box_plot(data, ['Weight', 'Height'])
