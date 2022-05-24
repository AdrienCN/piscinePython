from FileLoader import FileLoader


class SpatioTemporalData:

    def __init__(self, dataframe):
        self.df = dataframe

    def when(self, city):
        try:
            year = self.df[['City', 'Year']]
            year = year.loc[(year['City'] == city)]['Year']
            year_list = year.drop_duplicates()
            return year_list.to_list()
        except Exception as msg:
            print(msg)
            return None

    def where(self, year):
        try:
            city = self.df.loc[(self.df['Year'] == year)]['City']
            return(city.to_list()[0])
        except Exception as msg:
            print(msg)
            return None


loader = FileLoader()
data = loader.load("athlete_events.csv")

sp = SpatioTemporalData(data)
print(sp.where(2000))
print(sp.where(1980))
print(sp.when("London"))
