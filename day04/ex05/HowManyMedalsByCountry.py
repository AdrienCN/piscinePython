from FileLoader import FileLoader
import pandas as pd
import sys


def howManyMedalsByCountry(data, country):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming','Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']
    dico = {}
    df_country = data.loc[(data['Team'] == country)]
    df_country = df_country.sort_values('Year')
    df_country = df_country[['Year', 'Sex', 'Sport', 'Medal']]

    df_team = df_country.loc[(df_country['Sport'].isin(team_sports))]
    df_indiv = df_country.loc[~(df_country['Sport'].isin(team_sports))]
    
    year_list = df_country['Year'].drop_duplicates().to_list()
    for year in year_list:
        df_team_year = df_team.loc[(df_team['Year'] == year)].drop_duplicates()
        df_indiv_year = df_indiv.loc[(df_indiv['Year'] == year)]
        df_medal_total = pd.concat([df_team_year, df_indiv_year])
        medal_list = df_medal_total['Medal'].to_list()
        dico[year] = {'G':0, 'S':0, 'B':0}
        for medal in medal_list:
            if medal == 'Gold':
                dico[year]['G'] += 1
            elif medal == 'Silver':
                dico[year]['S'] += 1
            elif medal == 'Bronze':
                dico[year]['B'] += 1
    return dico

loader = FileLoader()
data = loader.load("athlete_events.csv")

if (len(sys.argv) != 2):
    print("Usage : <athlete's name>")
    quit()

name = sys.argv[1]
_dict = howManyMedalsByCountry(data, name)
for key, value in _dict.items():
    print(key, " : ", value)
