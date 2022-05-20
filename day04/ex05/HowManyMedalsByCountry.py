from FileLoader import FileLoader
import pandas as pd
import sys

def howManyMedalsByCountry(data, name):
    # Get all row where name == name
    df = data.loc[data['Team'] == name]
    df = df[['Year', 'Sex', 'Event', 'Medal']]
    print(df)
    dico = {}
    df = df.sort_values('Year')
    male_df = df.loc[(df['Sex'] == 'M')]
    female_df = df.loc[(df['Sex'] == 'F')]
    male_df = male_df.drop_duplicates('Event')
    female_df = female_df.drop_duplicates('Event')
    print(male_df)
    print(female_df)
    df = pd.concat([male_df, female_df])
    print(df)
    year_list = df['Year']
    year_list = year_list.drop_duplicates().to_list()
    print(year_list)
    for year in year_list:
        dico[year] = {'G':0, 'S':0, 'B':0}
        medal_df = df.loc[(df['Year'] == year)]
        #print(medal_df)
        medal_list = medal_df['Medal'].to_list()
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
#print(data.loc[(data['Team'] == "China")])
_dict = howManyMedalsByCountry(data, name)
for key, value in _dict.items():
    print(key, " : ", value)
