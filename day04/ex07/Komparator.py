from FileLoader import FileLoader
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def wrong_params(category, numerical, dataset):
    if not isinstance(numerical, str)\
            or not isinstance(category, str):
        print("Error : Wrong params : category and numerical must be str")
        return 1
    try:
        is_valid = dataset[category]
        is_numeric = dataset[numerical]
        if not isinstance(is_numeric.min(), (int, float)):
            print("Error : Wrong params : numerical is not int or float")
            return 1
    except Exception as msg:
        print("Error : Wrong params : {} or {} not in dataset : {}"
              .format(category, numerical))
        return 1
    return 0


class Komparator():

    def __init__(self, dataset):
        self.data = dataset

    def compare_box_plots(self, categorical_var, numerical_var):
        if wrong_params(categorical_var, numerical_var, self.data):
            return 1
        cat = categorical_var
        cat_list = self.data[cat].drop_duplicates().dropna().to_list()
        nb_list = [i for i in range(len(cat_list))]
        plot_list = []
        for subcat in cat_list:
            to_plot = self.data[[cat, numerical_var]].dropna()
            to_plot = to_plot.loc[(to_plot[cat] == subcat)]
            to_plot = to_plot[numerical_var]
            plot_list.append(to_plot)
        plt.boxplot(plot_list)
        plt.xticks([i + 1 for i in range(len(cat_list))], cat_list)
        plt.ylabel(numerical_var)
        plt.title(f"{numerical_var} repartion among {cat}(s)")
        plt.show()
        return 0

    def density(self, categorical_var, numerical_var):
        if wrong_params(categorical_var, numerical_var, self.data):
            return 1
        cat = categorical_var
        cat_list = self.data[cat].drop_duplicates().dropna().to_list()
        for subcat in cat_list:
            to_plot = self.data[[cat, numerical_var]].dropna()
            to_plot = to_plot.loc[(to_plot[cat] == subcat)]
            to_plot = to_plot[numerical_var]
            sns.kdeplot(to_plot, label=subcat)
        plt.ylabel("Density")
        plt.xlabel(numerical_var)
        plt.legend(title=cat)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        if wrong_params(categorical_var, numerical_var, self.data):
            return 1
        cat = categorical_var
        cat_list = self.data[cat].drop_duplicates().dropna().to_list()
        for subcat in cat_list:
            to_plot = self.data[[cat, numerical_var]].dropna()
            to_plot = to_plot.loc[(to_plot[cat] == subcat)]
            to_plot = to_plot[numerical_var]
            # Different figures options
            """
            plt.hist(to_plot, label=sub_cat)
            plt.legend(title=numerical_var)
            plt.show()
            """
            # Same figure options
            plt.hist(to_plot, histtype='step', label=subcat, stacked=True)
        plt.xlabel(numerical_var)
        plt.ylabel(f"Number of {cat}")
        plt.legend(title=cat)
        plt.show()
        return 0


loader = FileLoader()
data = loader.load("athlete_events.csv")
kpt = Komparator(data)
kpt.compare_histograms('Medal', 'Age')
kpt.compare_box_plots('Medal', 'Height')
kpt.density('Medal', 'Weight')
