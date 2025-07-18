import sys
import os

from sklearn.metrics import adjusted_rand_score
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))

from clusteringHelp import read_clusters, define_list_of_tag
from sklearn.cluster import KMeans
from models import CAMEMBERT, CODEBERT, SBERT, vectorize


args = sys.argv

model = CAMEMBERT

if(len(args) < 2):
    print("Not enough arguments please add one or two clustering's files")
    exit(1)

lst = define_list_of_tag(args[1])
pred = read_clusters(args[1], lst)
if(len(args) >= 3):
    groundtruth = read_clusters(args[2], lst)
    print("Rand Score = " + str(adjusted_rand_score(groundtruth, pred)))

else:
    vectors = vectorize(model, lst)
    means = KMeans(max(pred) + 1,n_init=20).fit(vectors)
    labels = means.labels_
    print("Rand Score = " + str(adjusted_rand_score(pred, labels)))