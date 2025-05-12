from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM

import random

import math

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import numpy as np






def dot_product(vec1, vec2):
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

def norm(vec):
    return math.sqrt(sum(v * v for v in vec))

def cosine_distance(vec1, vec2): # 0 si deux vecteurs identique, 1.0 = distance maximale.
    dp = dot_product(vec1, vec2)
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 1.0  # distance maximale si un vecteur est nul
    cosine_similarity = dp / (norm1 * norm2)
    return 1 - cosine_similarity  # distance cosinus

def moyenne(output):
    ret = output[0]
    for i in range(1, len(output)):
        ret = [ret[j] + output[i][j] for j in range(len(ret))]
    return [elem / len(output) for elem in ret]
print(moyenne([[10, 5, 2], [2, 5, 3], [10, 2, 4]]))


camembertav2 = AutoModel.from_pretrained("almanach/camembertav2-base")
tokenizer = AutoTokenizer.from_pretrained("almanach/camembertav2-base")
inputs = tokenizer("entrées clavier, conversion de chaines de caractères, opérations numériques, import de bibliothèque", return_tensors="pt")
inputs2 = tokenizer("input, operations, cast, import", return_tensors="pt")
tokens = inputs.tokens()
tokens2 = inputs2.tokens()



outputs = camembertav2(**inputs)
outputs2 = camembertav2(**inputs2)

def define_tags(tokens, outputs):
    dict = {}
    garbage = []
    tag = []
    vectors = []
    tokens_for_camembert = []

    for i in range(len(tokens)):
        tokens_for_camembert.append(tokens[i])
        if not tokens[i].startswith("["):
            if(tokens[i].startswith(",")):
                dict[tuple(moyenne(vectors))] = tag
                tag =[]
                vectors = []
            else:
                tag.append(tokens[i])
                vectors.append(outputs[0][0][i].detach().numpy().tolist())
        else:
            garbage.append(tokens[i])
            if(len(tag) > 0):
                dict[tuple(moyenne(vectors))] = tag
                tag =[]
                vectors = []
    return dict

def print_values(dict):
    for elem in dict:
        print(dict[elem])

def dict_to_cluster(dict):
    for elem in dict:
        print ("Cluster:")
        print(dict[elem])



def kmeans(i, dict):
    means = KMeans(i).fit(list(dict.keys()))

    bla = {}
    for n in range(i):
        bla[n] = []

    labels = means.labels_
    print (labels)
    print(bla)
    for i in range(len(dict.keys())):
        bla[labels[i]].append(dict[list(dict.keys())[i]])
    print(bla)

def hierarchical_clustering(i, dict):
    clustering = AgglomerativeClustering(n_clusters=i,linkage="single").fit(list(dict.keys()))
    labels = clustering.labels_
    bla = {}
    for n in range(i):
        bla[n] = []
    for i in range(len(dict.keys())):
        bla[labels[i]].append(dict[list(dict.keys())[i]])
    dict_to_cluster(bla)
    from_children_to_tree(clustering.children_, len(clustering.labels_), dict)

def from_children_to_tree(children, nb_labels, refs):
    lst = list(refs.keys())
    dico = {}
    for i in range(nb_labels):
        dico[i] = [refs[lst[i]]]
    i = nb_labels
    for elem in children:
        dico[i] = dico[elem[0]] + dico[elem[1]]
        print("Etape " + str(i - nb_labels) + " : Cluster Construit ")
        print (dico[i])
        i += 1

def DBScan(dict):
    dico = {}
    lst = list(dict.keys())
    model = DBSCAN(eps=5.0, min_samples=2) # 6 à l'air d'être un epsilon raisonnable peut être à légerement ajuster
    model.fit(lst)
    labels = model.labels_
    print(labels)
    lst = [dict[elem] for elem in lst]
    print(lst)        


tags1 = define_tags(tokens, outputs)
tags2 = define_tags(tokens2, outputs2)


print("first")
print_values(tags1)
print("second")
print_values(tags2)
print("thirs")
tags3 = tags1 | tags2
print_values(tags3)

kmeans(4, tags3)
hierarchical_clustering(4, tags3)
DBScan(tags3)