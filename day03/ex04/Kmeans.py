import numpy as np
import csv
import sys


def check_params(ncentroid, max_iter):
    if len(ncentroid) != 2 or len(max_iter) != 2:
        return 0
    if not ncentroid[0] == "ncentroid" or max_iter[0] != "max_iter":
        return 0
    if not ncentroid[1].isdigit() or not max_iter[1].isdigit():
        return 0
    return 1


if (len(sys.argv) != 4):
    print("Error : Usage : <file_path.csv> <ncentroid=int> <max_iter=int>")
    exit(1)
path = sys.argv[1]
try :
    with open (path) as csv_file:
        reader = csv.DictReader(csv_file, ['index', 'height', 'weight', 'bone_density'])
        #for row in reader:
         #   print("index : {:3} | height {:3.3} | weight {:3.3} | bone {:3.3}".format(row["index"], row["height"], row["weight"], row["bone_density"]))
        ncentroid = sys.argv[2].split("=")
        max_iter = sys.argv[3].split("=")
        if not check_params(ncentroid, max_iter):
            raise ValueError("Usage : <ncentroid=int> <max_iter=int>")


except Exception as msg:
    print("Error : ", msg)
    exit(1)
