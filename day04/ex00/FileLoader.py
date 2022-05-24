import pandas as pd


class FileLoader():

    def __init__(self):
        pass

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensions {}x{}"
                  .format(len(df), len(df.columns)))
            return df
        except Exception as msg:
            print(msg)
            return None

    def display(self, df, n):
        try:
            if n >= 0:
                print(df.head(n))
            else:
                print(df.tail(abs(n)))
        except Exception as msg:
            print(msg)
            return None


loader = FileLoader()
data = loader.load("athlete_events.csv")
loader.display(data, 12)
