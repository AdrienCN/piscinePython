from FileLoader import FileLoader
from YoungestFellah import youngestfellah
import sys

loader = FileLoader()
data = loader.load("athlete_events.csv")
try:
    print("Expected output is:\n{'f': 12.0, 'm': 11.0}")
    print(youngestfellah(data, 1992))

    print("\nExpected output is:\n{'f': 13.0, 'm': 14.0}")
    print(youngestfellah(data, 2004))

    print("\nExpected output is:\n{'f': 15.0, 'm': 15.0}")
    print(youngestfellah(data, 2010))

    print("\nExpected output is:\n{'f': nan, 'm': nan}")
    print(youngestfellah(data, 2003))

    sys.exit(0)
except Exception as msg:
    print(msg)
    sys.exit(1)
