from FileLoader import FileLoader
from YoungestFellah import youngestfellah
import sys

if len(sys.argv) != 3:
    print("Usage : python3 main.py <path_to_csv_file> <year>")
    quit()

path = sys.argv[1]
loader = FileLoader()
data = loader.load(path)
if data is None:
    quit()
res = youngestfellah(data, int(sys.argv[2]))
print("Dict : ", res)
