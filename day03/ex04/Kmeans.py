import numpy as np
import csv
import random
import copy
import sys
from csvreader import CsvReader
from matplotlib import pyplot as plt


def check_params(ncentroid, max_iter):
    if len(ncentroid) != 2 or len(max_iter) != 2:
        return 0
    if not ncentroid[0] == "ncentroid" or max_iter[0] != "max_iter":
        return 0
    if not ncentroid[1].isdigit() or not max_iter[1].isdigit():
        return 0
    return 1

def get_distance(data_point, centroids, min_list, max_list):
    # Pour chaque centroid
    distance = []
    ret = 0
    x_range = max_list[0] - min_list[0]
    y_range = max_list[1] - min_list[1]
    z_range = max_list[2] - min_list[2]
    x_norm_1 = (data_point[0] - min_list[0]) / x_range
    y_norm_1 = (data_point[1] - min_list[1]) / y_range
    z_norm_1 = (data_point[2] - min_list[2]) / z_range
    for i in range(len(centroids)):
        x_norm_2 = (centroids[i][0] - min_list[0]) / x_range
        y_norm_2 = (centroids[i][1] - min_list[1]) / y_range
        z_norm_2 = (centroids[i][2] - min_list[2]) / z_range
        dst = np.square((x_norm_1 - x_norm_2)**2 +
                        (y_norm_1 - y_norm_2)**2 +
                        (z_norm_1 - z_norm_2)**2)
        distance.append(dst)
        if dst < distance[ret]:
            ret = i
    return ret

def     get_mean(cluster, X):
    #Pour chaque data dans mon cluster
    x = 0.0
    y = 0.0
    z = 0.0
    c_len = len(cluster)
    if c_len == 0:
        index = random.randint(0,X.shape[0] - 1)
        return X[index]
    for i in range(c_len):
        x += X[cluster[i]][0]
        y += X[cluster[i]][1]
        z += X[cluster[i]][2]
    x = x / c_len
    y = y / c_len
    z = z / c_len
    return [x, y, z]
 

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # iteration max to updates centroids
        self.centroids = [] # centroids values
        self.clusters = [[] for i in range(self.ncentroid)]
        
     
    def fit(self, X):
        self.min_list = np.amin(X, 0)
        self.max_list = np.amax(X, 0)
        # Get centroids random value from within dataset
        for i in range(self.ncentroid):
            index = random.randint(0, X.shape[0] - 1)
            self.centroids.append(X[index].tolist())
        prev_centroids = []
        for iteration in range(self.max_iter):
            data_arr = self.predict(X)
            new_centroids = self.get_clusters_means(data_arr, X)
            if np.array_equal(np.array(new_centroids), np.array(self.centroids)):
                break
            self.centroids = new_centroids
        self.display_result()
        return

    def predict(self, X):
        predict = np.zeros((X.shape[0], 1))
        for i in range(X.shape[0]):
            predict[i] = get_distance(X[i], self.centroids,
                                      self.min_list, self.max_list)
        count = [0, 0, 0, 0]
        for i in range(predict.shape[0]):
            count[int(predict[i][0])] += 1
        return predict

    def get_clusters_means(self, data_arr, X):
        self.clusters.clear()
        self.clusters= [[] for i in range(self.ncentroid)]
        for i in range(data_arr.shape[0]):
            self.clusters[int(data_arr[i][0])].append(i)
        means = [[] for i in range(self.ncentroid)]
        for i in range(self.ncentroid):
            means[i] = get_mean(self.clusters[i], X)
        return means

    def display_result(self):
        if (self.ncentroid == 4):
            belt = max(x[0] for x in self.centroids)
            earth = min(x[0] for x in self.centroids)
            for i in range(len(self.centroids)):
                if earth in self.centroids[i]:
                    earth = i
                elif belt in self.centroids[i]:
                    belt = i
            venus = -1
            mars = -1
            for i in range(len(self.centroids)):
                if i == belt or i == earth:
                    pass
                else:
                    if venus == -1:
                        venus = i
                    else:
                        mars = i
            if self.centroids[venus][0] > self.centroids[earth][0]\
                and self.centroids[venus][1] < self.centroids[earth][1]:
                    pass
            else:
                tmp = mars
                mars = venus
                venus = tmp
            print("\nmars : {} | earth {} | venus {} | belt {}\n".format(mars, earth, venus, belt))

            print(" -Mars   : K[{}] : val {}  : {}\n"
                  .format(mars, self.centroids[mars], len(self.clusters[mars])),
                  "-Belt   : K[{}] : val {}   : {}\n"
                  .format(belt, self.centroids[belt], len(self.clusters[belt])),
                  "-Earth  : K[{}] : val {}   : {}\n"
                  .format(earth, self.centroids[earth], len(self.clusters[earth])),
                  "-Venus  : K[{}] : val {}   : {}\n"
                  .format(venus, self.centroids[venus], len(self.clusters[venus])))
    
def plot_res_3d(X, kmeans):
    
    predict = kmeans.predict(X)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    color= ["lightpink", "cyan", "lightgreen", "salmon"]
    for j in range(0, kmeans.ncentroid):
        for i in range(X.shape[0]):
            if predict[i] == j:
                ax.scatter(X[i][0], X[i][1], X[i][2], c=color[j % 4])
    color2= ["magenta", "b", "g", "r"]
    for i in range(0, kmeans.ncentroid):
        ax.scatter(kmeans.centroids[i][0], kmeans.centroids[i][1], kmeans.centroids[i][2], c=color2[i % 4])
    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Bone")
    plt.show()

if (len(sys.argv) != 4):
    print("Error : Usage : <file_path.csv> <ncentroid=int> <max_iter=int>")
    exit(1)
path = sys.argv[1]
try :
    with CsvReader(path, ",", True) as csv_file:
        if csv_file == None:
            print("file could not be opened")
            exit()
        ncentroid = sys.argv[2].split("=")
        max_iter = sys.argv[3].split("=")
        if not check_params(ncentroid, max_iter):
            raise ValueError("Usage : <ncentroid=int> <max_iter=int>")
        ncentroid = int(ncentroid[1])
        max_iter = int(max_iter[1])
        data_arr = np.array(csv_file.getdata(), dtype=float)
        data_arr = np.delete(data_arr, 0, 1)
        k = KmeansClustering(max_iter, ncentroid)
        k.fit(data_arr)
        plot_res_3d(data_arr, k)
except Exception as msg:
    print("Error : ", msg)
    exit(1)
