import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from FileLoader import FileLoader
import seaborn as sns
#import scipy as sp

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
        return  1


class MyPlotLib:

    def __init__(self):
        pass

    def histogram(self, data, features):
        if wrong_params(data, features):
            return 1
        for var in features:
            data_var = data[['ID', var]].drop_duplicates().dropna()
            data_var = data_var[var]
            print(var)
            plt.hist(data_var,
                     range=[data_var.min(), data_var.max()],
                     edgecolor='black')
            plt.legend(title=var)
            plt.show()
        return 0

    def density(self, data, features):
        if wrong_params(data, features):
            return 1
        kde_list = []
        label_list = []
        for var in features:
            data_var = data[['ID', var]].drop_duplicates().dropna()
            data_var = data_var[var]
            kde_list.append(data_var)
            label_list.append(var)
            """
            plt.hist(data_var, range=[data_var.min(), data_var.max()], density=True)
            plt.legend(var)
            plt.show()
            """
        plt.figure()
        for i in range(len(kde_list)):
            sns.kdeplot(kde_list[i], label=label_list[i])
        plt.legend(labels=label_list)
        plt.show()
        return 0

    def pair_plot(self, data, features):
        pass

    def box_plit(self, data, features):
        pass

if len(sys.argv) !=  1:
    sys.exit("Usage : python3 <exec_file>")
loader = FileLoader()
data = loader.load("athlete_events.csv")
myplot = MyPlotLib()
myplot.histogram(data, ['Height', 'Weight'])
myplot.density(data, ['Height', 'Weight'])
