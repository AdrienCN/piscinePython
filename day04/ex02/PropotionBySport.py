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


if len(sys.argv) != 4:
    printf("Usage : <Year>, <Sport>, <Sex>")
    quit()

year = int(sys.argv[1])
sport = sys.argv[2]
sex = sys.argv[3]
loader = FileLoader()
df = loader.load("athlete_events.csv")

ret = proportionBySport(df, year, sport, sex)
print("Res : ", ret)
