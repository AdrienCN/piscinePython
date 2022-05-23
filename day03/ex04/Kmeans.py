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


# Calcul la moyenne de chaque nouveau centroids
def find_cluster_mean(cluster, X):
    x = 0.0
    y = 0.0
    z = 0.0
    c_len = len(cluster)
    if c_len == 0:
        index = random.randint(0, X.shape[0] - 1)
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
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    # Run the Kmeans Algo
    def fit(self, X):
        self.min_list = np.amin(X, 0)
        self.max_list = np.amax(X, 0)

        # Get centroids random value from within dataset
        for i in range(self.ncentroid):
            index = random.randint(0, X.shape[0] - 1)
            self.centroids.append(X[index].tolist())
        # Run the Kmeans algo
        prev_centroids = []
        for iteration in range(self.max_iter):
            predict_arr = self.predict(X)
            new_centroids = self.find_new_centroids(predict_arr, X)

            # Stop before max_iter if Kmeans is found
            if np.array_equal(np.array(new_centroids),
                              np.array(self.centroids)):
                break
            self.centroids = new_centroids
        self.display_result()
        return

    # Get distance between point to every centroids
    # Returns array with every point with index to its closest centroid
    def predict(self, X):
        predict = np.zeros((X.shape[0], 1))
        for i in range(X.shape[0]):
            predict[i] = get_distance(X[i], self.centroids,
                                      self.min_list, self.max_list)
        return predict

    def find_new_centroids(self, predict_arr, X):
        cluster = [[] for i in range(self.ncentroid)]
        # Cree une list de cluster contenant leurs
        # datapoints associe
        for datapoint in range(data_arr.shape[0]):
            idx = int(predict_arr[datapoint][0])
            cluster[idx].append(datapoint)
        new_centroids = []
        for i in range(self.ncentroid):
            new_centroids.append(find_cluster_mean(cluster[i], X))
        # To count individual a the end
        self.clusters = cluster
        return new_centroids

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
            self.mars = mars
            self.venus = venus
            self.earth = earth
            self.belt = belt

            print(" -Mars   : K[{}] : val {}  : {}\n"
                  .format(mars, self.centroids[mars],
                          len(self.clusters[mars])),
                  "-Belt   : K[{}] : val {}   : {}\n"
                  .format(belt, self.centroids[belt],
                          len(self.clusters[belt])),
                  "-Earth  : K[{}] : val {}   : {}\n"
                  .format(earth, self.centroids[earth],
                          len(self.clusters[earth])),
                  "-Venus  : K[{}] : val {}   : {}\n"
                  .format(venus, self.centroids[venus],
                          len(self.clusters[venus])))


def plot_res_3d(X, kmeans):

    predict = kmeans.predict(X)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for j in range(0, kmeans.ncentroid):
        for i in range(X.shape[0]):
            if predict[i] == kmeans.mars:
                color2 = "lightsalmon"
            elif predict[i] == kmeans.earth:
                color2 = "skyblue"
            elif predict[i] == kmeans.venus:
                color2 = "gold"
            elif predict[i] == kmeans.belt:
                color2 = "palegreen"
            else:
                color2 = "black"
            ax.scatter(X[i][0], X[i][1], X[i][2], c=color2)
    ax.scatter(kmeans.centroids[kmeans.mars][0],
               kmeans.centroids[kmeans.mars][1],
               kmeans.centroids[kmeans.mars][2],
               c="r", label="Mars")
    ax.scatter(kmeans.centroids[kmeans.earth][0],
               kmeans.centroids[kmeans.earth][1],
               kmeans.centroids[kmeans.earth][2],
               c="b", label="Earth")
    ax.scatter(kmeans.centroids[kmeans.venus][0],
               kmeans.centroids[kmeans.venus][1],
               kmeans.centroids[kmeans.venus][2],
               c="orange", label="Venus")
    ax.scatter(kmeans.centroids[kmeans.belt][0],
               kmeans.centroids[kmeans.belt][1],
               kmeans.centroids[kmeans.belt][2],
               c="green", label="Belt")

    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Bone")
    plt.legend()
    plt.show()


if (len(sys.argv) != 4):
    print("Error : Usage : <file_path.csv> <ncentroid=int> <max_iter=int>")
    exit(1)
path = sys.argv[1]
try:
    with CsvReader(path, ",", True) as csv_file:
        if csv_file is None:
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
