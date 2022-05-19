from FileLoader import FileLoader

class SpatioTemporalData: 
    def __init__(self, dataframe):
        self.df = dataframe

    def when(self, city):
        year = self.df[['City', 'Year']]
        year = year.loc[(year['City'] == city)]['Year']
        #year_list = []
        #year = year.to_list()
        #[year_list.append(x) for x in year if x not in year_list]
        year_list = year.drop_duplicates()
        return year_list

    def where(self, year):
        city = self.df.loc[(self.df['Year'] == year)]['City']
        return(city.to_list()[0])


loader = FileLoader()
data = loader.load("athlete_events.csv")

sp = SpatioTemporalData(data)
print(sp.where(2016))
print(sp.when("Paris"))

