from FileLoader import FileLoader
import pandas as pd
import sys

"""
def howManyMedalsByCountry(data, name):
    # Get all row where name == name
    df = data.loc[data['Team'] == name]
    df = df[['Year', 'Sex', 'Event', 'Medal']]
    print(df)
    dico = {}
    df = df.sort_values('Year')
    df.dropna(inplace=True)
    #df = pd.concat([male_df, female_df])
print(df)
    year_list = df['Year'].drop_duplicates().to_list()
    for year in year_list:
        dico[year] = {'G':0, 'S':0, 'B':0}
 
        # Get df for a specific year
        df_year = df.loc[(df['Year'] == year)]
        # Get all male & female from this year
        male_df = df_year.loc[(df_year['Sex'] == 'M')]
        female_df = df_year.loc[(df_year['Sex'] == 'F')]
        # Drop duplicates for each category
        male_df = male_df.drop_duplicates('Event')
        female_df = female_df.drop_duplicates('Event')
        
        #Merge les deux sans duplicats
        df_year = pd.concat([male_df, female_df])
        print(df_year)
        #Recupere tout les medailles de cette annee
        medal_list = df_year['Medal'].to_list()
        for medal in medal_list:
            if medal == 'Gold':
                dico[year]['G'] += 1
            elif medal == 'Silver':
                dico[year]['S'] += 1
            elif medal == 'Bronze':
                dico[year]['B'] += 1
    return dico
"""
def howManyMedalsByCountry(data, country):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming','Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']

    dico = {}
    df = data.loc[(data['Team'] == country)]
    df = df.sort_values('Year')
    df.dropna(inplace=True)
    df = df[['Year', 'Sex', 'Sport','Medal', 'Event']]
    df_team = df.loc[(df['Sport'].isin(team_sports))]
    df_indiv = df.loc[~(df['Sport'].isin(team_sports))]
    year_list = df['Year'].drop_duplicates().to_list()
    for year in year_list:
        df_team_year = df_team.loc[(df_team['Year'] == year)].drop_duplicates('Event')
        df_indiv_year = df_indiv.loc[(df_indiv['Year'] == year)]
        df_medal_total = pd.concat([df_team_year, df_indiv_year])
        print("Year {} Team :\n{}".format(year, df_team_year)) 
        print("Year {} Indiv :\n{}".format(year, df_indiv_year)) 
        print("\t*****\nMedal total :\n", df_medal_total)
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
#print(data.loc[(data['Team'] == "China")])
_dict = howManyMedalsByCountry(data, name)
for key, value in _dict.items():
    print(key, " : ", value)
