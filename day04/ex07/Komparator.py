from FileLoader import FileLoader
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def wrong_params(category, numerical):
    if not isinstance(numerical, list)\
        or not isinstance(category, list):
            print("Error : Wrong params")
            return 1
    for elem in category:
        if not isinstance(elem, str):
            print("Error : Wrong params")
            return 1
    for elem in numerical:
        if not isinstance(elem, str):
            print("Error : Wrong params")
            return 1
    return 0


class Komparator():
    
    def __init__(self, dataset):
        self.data  =  dataset

    def compare_box_plots(self, categorical_var, numerical_var):
        pass

    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        if wrong_params(categorical_var, numerical_var):
            return 1
        #get the category SEX
        for pop in categorical_var:
            #get all subcategory M or  F
            poplist = self.data[pop].drop_duplicates().dropna().to_list()
            for subpop in poplist:
                #get a hist for every value (Height, Weight ...)
                to_plot = None
                for feature in numerical_var:
                    to_plot = self.data[[pop, feature]].dropna()
                    to_plot = to_plot.loc[(to_plot[pop] == subpop)]
                    print("plotting : {} : {} : ".format(subpop, feature))
                plt.hist(to_plot, label=subpop)
            plt.legend()
            plt.show()
        print("showing graph")

loader = FileLoader()
data = loader.load("athlete_events.csv")
kpt = Komparator(data)
kpt.compare_histograms(['Medal'], ['Age'])
