
import sys
import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))

from models import vectorize, CODEBERT, get_dict_vectors

def solution(PATH, pattern, nb):

    sentences = []

    for i in range(1, nb):
        file_name = pattern + str(i) + ".py"
        f = open(PATH + file_name, 'r')
        sentences.append(f.read())
        f.close()
    return sentences


args = sys.argv

if(len(args) < 4 ):
    print("Not enough arguments please put the PATH and the pattern for the files Name and the number of files")
    exit(1)




dico = get_dict_vectors(CODEBERT, solution(args[1], args[2], int(args[3])))
keys = []
tsne = TSNE(perplexity=20)
for elem in dico:
    keys.append(np.array(elem))
X_embedded = tsne.fit_transform(np.array(keys))
plt.scatter(X_embedded[:,0], X_embedded[:,1])
plt.show()
