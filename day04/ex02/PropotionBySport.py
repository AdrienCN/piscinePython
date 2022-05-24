from FileLoader import FileLoader
import pandas as pd
import sys


def proportionBySport(df, year, sport, sex):
    df_sex = df.loc[(df['Sex'] == sex) & (df['Year'] == year)]
    _all = df_sex.shape[0]
    df_zoom = df_sex.loc[df_sex['Sport'] == sport]
    group = df_zoom.shape[0]
    proportion = group / _all
    return proportion


loader = FileLoader()
data = loader.load("athlete_events.csv")

print("Expected output is :\n0.02307...")
print(proportionBySport(data, 2004, 'Tennis', 'F'), end = "\n\n")

print("Expected output is :\n0.03284...")
print(proportionBySport(data, 2008, 'Hockey', 'F'), end = "\n\n")

print("Expected output is :\n0.00659...")
print(proportionBySport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
