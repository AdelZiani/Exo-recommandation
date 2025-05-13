from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM

import random

import math
from sklearn.metrics import silhouette_score

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import numpy as np

camembert = "almanach/camembertav2-base"




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


camembertav2 = AutoModel.from_pretrained(camembert)
tokenizer = AutoTokenizer.from_pretrained(camembert)
inputs1 = tokenizer("import de bibliothèque, initialisation de variable, input de données, cast, type float, calcul avec PI, division réel, affichage écran texte et valeur d'une variable, appel fonction print, opérateur arithmétique /, opérateur arithmétique *", return_tensors="pt")
inputs2 = tokenizer("initialisation de variable, input de données, cast, type float, boucle while, affichage écran texte et valeur formaté d'une variable, appel fonction print, opérateur arithmétique *, condition booléen, opérateur booléen >", return_tensors="pt")
inputs3 = tokenizer("initialisation de variable, input de données, cast, type int, boucle while, affichage écran texte et valeur formaté d'une variable, appel fonction print, opérateur arithmétique *, condition booléen, opérateur booléen >, opérateur arithmétique +, affectation de variable, conditionnel, calcul d'une somme d'entier.", return_tensors="pt")
inputs4 = tokenizer("input, variables, operations, cast, import", return_tensors="pt")
inputs5 = tokenizer("input, variables, while, operations, cast", return_tensors="pt")
inputs6 = tokenizer("while, comparaison, incrémentation, cast, if, comparaison, input, variable", return_tensors="pt")
inputs7 = tokenizer("entrées clavier, conversion de chaines de caractères, opérations numériques, import de bibliothèque", return_tensors="pt")
inputs8 = tokenizer("boucle while, entrée clavier, conversion de chaines de caractères, opérations numériques", return_tensors="pt")
inputs9 = tokenizer("boucle while, entrée clavier, conversion de chaines de caractères, opérations numériques, incrémentation d'une variable", return_tensors="pt")
inputs1 = tokenizer("Président", return_tensors="pt")
inputs2 = tokenizer("Directeur général", return_tensors="pt")
inputs3 = tokenizer("Ministre", return_tensors="pt")
inputs4 = tokenizer("fruit du dragon", return_tensors="pt")
inputs5 = tokenizer("poire", return_tensors="pt")
inputs6 = tokenizer("pomme", return_tensors="pt")
inputs7 = tokenizer("haut-parleur", return_tensors="pt")
inputs8 = tokenizer("écran", return_tensors="pt")
inputs9 = tokenizer("unité centrale", return_tensors="pt")

tokens1 = inputs1.tokens()
tokens2 = inputs2.tokens()
tokens3 = inputs3.tokens()
tokens4 = inputs4.tokens()
tokens5 = inputs5.tokens()
tokens6 = inputs6.tokens()
tokens7 = inputs7.tokens()
tokens8 = inputs8.tokens()
tokens9 = inputs9.tokens()



outputs1 = camembertav2(**inputs1)
outputs2 = camembertav2(**inputs2)
outputs3 = camembertav2(**inputs3)
outputs4 = camembertav2(**inputs4)
outputs5 = camembertav2(**inputs5)
outputs6 = camembertav2(**inputs6)
outputs7 = camembertav2(**inputs7)
outputs8 = camembertav2(**inputs8)
outputs9 = camembertav2(**inputs9)



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


#on prend que les [CLS]
def take_cls(tokens, outputs):
    dict = {}
    dict[tuple(outputs[0][0][0].detach().numpy().tolist())] = tokens
    return dict



def print_values(dict):
    for elem in dict:
        print(dict[elem])

def dict_to_cluster(dict):
    for elem in dict:
        print ("Cluster:")
        print(dict[elem])


def get_values(keys, dico):
    ret = []
    for elem in keys:
        ret.append(dico[elem])
    return ret


def kmeans(i, dico):
    keys = list(dico.keys())
    values = get_values(keys, dico)
    means = KMeans(i,n_init=20).fit(keys)
    labels = means.labels_
    print_cluster(values, labels)

def hierarchical_clustering(i, dico):
    keys = list(dico.keys())
    values = get_values(keys, dico)
    clustering = AgglomerativeClustering(n_clusters=i).fit(keys)
    labels = clustering.labels_
    print_cluster(values, labels)
    from_children_to_tree(clustering.children_, len(clustering.labels_), dico)


def from_children_to_tree(children, nb_labels, refs):
    lst = list(refs.keys())
    dico = {}
    for i in range(nb_labels):
        dico[i] = [refs[lst[i]]]
    i = nb_labels
    for elem in children:
        values = get_values(lst, refs)
        dico[i] = dico[elem[0]] + dico[elem[1]]
        dico.pop(elem[0])
        dico.pop(elem[1])

        print("Etape " + str(i - nb_labels) + " : ")
        print("     Cluters existants:")
        print("                 " + str(values))
        print("      Cluster Construit:")
        print ("                " + str(dico[i]))
        i += 1


def DBScan(dict):
    dico = {}
    lst = list(dict.keys())
    values = get_values(lst, dict)
    model = DBSCAN(eps=5.0, min_samples=2) # 6 à l'air d'être un epsilon raisonnable peut être à légerement ajuster
    model.fit(lst)
    labels = model.labels_
    print_cluster(values, labels)


def print_cluster(values, clusters):
    true_values = []
    dico = {}
    for elem in values:
        tag = ""
        for token in elem:
            tag+=token
        true_values.append(tag)
    for i in range (len(clusters)):
        dico.setdefault(clusters[i], []).append(true_values[i])
    for key in dico:
        print("\n\n")
        if key == -1:
            print("Noise----------------------------------------------\n")
        else:    
            print("Cluster -------------------------------------------\n")
        
        for elem in dico[key]:
            print(elem)
    print("\n\n")

tags1 = define_tags(tokens1, outputs1)
tags2 = define_tags(tokens2, outputs2)
tags3 = define_tags(tokens3, outputs3)
tags4 = define_tags(tokens4, outputs4)
tags5 = define_tags(tokens5, outputs5)
tags6 = define_tags(tokens6, outputs6)
tags7 = define_tags(tokens7, outputs7)
tags8 = define_tags(tokens8, outputs8)
tags9 = define_tags(tokens9, outputs9)

print("first")
print_values(tags1)
print("second")
print_values(tags4)
print("thirs")
print_values(tags7)





tagsnew = tags1 | tags2 | tags3 | tags4 | tags5 | tags6 | tags7 | tags8 | tags9
print_values(tagsnew)


print("\nkmeans +++++++++++++++++++++++++++++++++++++++++++++\n")
kmeans(3, tagsnew)
print("\nhierarchical ++++++++++++++++++++++++++++++++++++++++++++\n")
hierarchical_clustering(3, tagsnew)
print("\nDBSCAN ++++++++++++++++++++++++++++++++++++++++++\n")
DBScan(tagsnew)