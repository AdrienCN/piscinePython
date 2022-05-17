import numpy as np
import csv
import random
import copy
import sys
from csvreader import CsvReader


def check_params(ncentroid, max_iter):
    if len(ncentroid) != 2 or len(max_iter) != 2:
        return 0
    if not ncentroid[0] == "ncentroid" or max_iter[0] != "max_iter":
        return 0
    if not ncentroid[1].isdigit() or not max_iter[1].isdigit():
        return 0
    return 1

def get_distance(data_point, centroids):
    # Pour chaque centroid
    distance = []
    ret = 0
    for i in range(len(centroids)):
        #dst = np.square((data_point[0] - centroids[i][0])**2 + (data_point[1] - centroids[i][1])**2 + (data_point[2] - centroids[i][2])**2)
        #dst = np.absolute(data_point[0] - centroids[i][0]) + np.absolute(data_point[1] - centroids[i][1]) + np.absolute(data_point[2] - centroids[i][2])
        dst = abs(data_point[0] - centroids[i][0]) + abs(data_point[1] - centroids[i][1]) + abs(data_point[2] - centroids[i][2])
        distance.append(dst)
        if dst < distance[ret]:
            ret = i
    #print("ret : ", ret)
    return ret

def     get_mean(cluster, X):
    #Pour chaque data dans mon cluster
    x = 0.0
    y = 0.0
    z = 0.0
    c_len = len(cluster)
    if c_len == 0:
        return [0, 0, 0]
    for i in range(c_len):
        x += X[cluster[i]][0]
        z += X[cluster[i]][1]
        y += X[cluster[i]][2]
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

    def get_clusters_means(self, data_arr, X):
        self.clusters.clear()
        self.clusters= [[] for i in range(self.ncentroid)]
        # rempli nos clusters avec les index
        for i in range(data_arr.shape[0]):
            self.clusters[int(data_arr[i][0])].append(i)
            #edge case cluster is empty after update

        means = [[] for i in range(self.ncentroid)]
        print("\t***************************")
        for i in range(self.ncentroid):
            means[i] = get_mean(self.clusters[i], X)
            print("cluster{}\n-len : {}\n-Means : {}\n {}\n".format(i, len(self.clusters[i]), means[i], self.clusters[i]))
        print("\t***************************")
        return means

    def display_result(self):
        for i in range(self.ncentroid):
            print("Centroid [{}] : \n- coordinate {}\n- individuals {}.\n"
                  .format(i, self.centroids[i], len(self.clusters[i])))
    
    def centroids_are_equal(self, cluster_mean, centroids):
        for i in range(self.ncentroid):
            tmp = list(centroids[i])
            if cluster_mean[i] != tmp:
                return 0
        return 1
    
    def fit(self, X):
        # Get centroids random value from within dataset
        for i in range(self.ncentroid):
            index = random.randint(0, X.shape[0] - 1)
            self.centroids.append(X[index])
            print("Init centroid {} : {} --- Index {}".format(i, self.centroids[i], index))
        for i in range(self.max_iter):
            data_arr = self.predict(X)
            cluster_mean = self.get_clusters_means(data_arr, X)
            if self.centroids_are_equal(cluster_mean, self.centroids):
                self.display_result()
                exit()
            self.centroids.clear()
            self.centroids = copy.deepcopy(cluster_mean)
        
        # Update centroid position 
        #for i in range(self.max_iter):
        # Create cluster that will be filled with closest datapoint
            # check si on a trouve le cluster optimum
            #if (centroids == cluster_predict):
            #    break
            #self.centroids.clear()
            #self.centroids = cluster_predict
        self.display_result()
        return

    def predict(self, X):
        predict = np.zeros((X.shape[0], 1))
        
        # Passer dans chaque ligne
        for i in range(X.shape[0]):
            #calculer la distance entre ce point et les 4 centroids
            # retourner l'index du centroids le + proche
            """
            index_closest_centroid = get_distance(X[i], self.centroids)
            clusters[index_closest_centroid].append(i)
            """
            predict[i] = get_distance(X[i], self.centroids)
        count = [0, 0, 0, 0]
        for i in range(predict.shape[0]):
            count[int(predict[i][0])] += 1;
        for i in range(len(count)):
            print("cluster[{}] : {}".format(i, count[i]))
        # Calculer la mean value pour chaque centroid et replacer les centroids value par cela
        """
        new_centroids = []
        for i in range(self.ncentroid):
            print("Cluster_mean : ", i)
            new_centroids[i] = get_mean(clusters[i], X)
    
        for i in range(len(new_centroids)):
            print("old i = {} : {}\n".format(i ,self.centroids[i]))
            print("new i = {} : {}\n\n".format(i ,new_centroids[i]))
        np_centroids = np.zeros((self.ncentroids
        """
        return predict

        
        



if (len(sys.argv) != 4):
    print("Error : Usage : <file_path.csv> <ncentroid=int> <max_iter=int>")
    exit(1)
path = sys.argv[1]
print(path)
try :
    with CsvReader(path, ",", True) as csv_file:
        #reader = csv.DictReader(csv_file, ['index', 'height', 'weight', 'bone_density'])
        #for row in reader:
         #   print("index : {:3} | height {:3.3} | weight {:3.3} | bone {:3.3}".format(row["index"], row["height"], row["weight"], row["bone_density"]))
        
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
        print(data_arr.shape)
        print(np.ndarray.flatten(data_arr))
        k = KmeansClustering(max_iter, ncentroid)
        k.fit(data_arr)
except Exception as msg:
    print("Error : ", msg)
    exit(1)
