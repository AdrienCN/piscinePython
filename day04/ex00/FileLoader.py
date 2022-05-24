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

    def display(df, n):
        try:
            if n > 0:
                df.head(n)
            else:
                df.tail(abs(n))
        except Exception as msg:
            print(msg)
            return None
