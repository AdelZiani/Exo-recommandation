from sklearn.metrics import adjusted_rand_score
from modules.clusteringHelp import read_clusters

groundtruth = read_clusters("Clusters.txt")
pred = read_clusters("ClustersChatGPT.txt")

print("Rand Score = " + str(adjusted_rand_score(groundtruth, pred)))