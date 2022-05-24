from FileLoader import FileLoader
import sys


def howManyMedals(data, name):
    # Get all row where name == name
    df = data.loc[data['Name'] == name]
    df_year = df['Year'].drop_duplicates()
    year_list = df_year.to_list()
    dico = {}
    for year in year_list:
        dico[year] = {'G': 0, 'S': 0, 'B': 0}
        medal_list = df.loc[(df['Year'] == year)]
        medal_list = medal_list['Medal'].to_list()
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

print("Expected output is:\n"
      " {1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}")
print("res:\n", howManyMedals(data, 'Gary Abraham'))

print("\nExpected output is:\n"
      " {2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}")
print("res:\n", howManyMedals(data, 'Yekaterina Konstantinovna Abramova'))

print("\nExpected output is:\n"
      " {1988: {'G': 6, 'S': 0, 'B': 0}}")

print("res\n", howManyMedals(data, 'Kristin Otto'))
