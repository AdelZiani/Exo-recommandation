from transformers import AutoTokenizer, AutoModel
import torch
import ast
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))
import csv

from models import *
from vectors_operations import cosine_distance

def cleanGit(code):
    while code.endswith("\n") or code.startswith("\n"):
        code= code.removesuffix("\n").removeprefix("\n")
    code = code.removeprefix("```python").removesuffix("```")
    return code


def enonces():
    PATH = "../../Exo-recommandation-data/données_exercices/exercices_autres/Github/enonces/"

    sentences = []

    for i in range(1, 101):
        file_name = "Github" + str(i) + ".txt"
        f = open(PATH + file_name, 'r')
        sentences.append(f.read())
        f.close()
    return sentences

def solution():
    PATH = "../all_exercices_27_06_2025"

    sentences = []

    for i in range(1, 100):
        file_name = "Github" + str(i) + ".py"
        f = open(PATH + file_name, 'r')
        text = f.read()
        print(text, i, "###################################")
        ast.parse(cleanGit(text))
        sentences.append(text)
        f.close()
    return sentences

"""
dico = vectorize(CAMEMBERT, enonces())
dico2 = vectorize(CODEBERT, solution())
dico3 = {}

for i in range(len(dico)):
    print(dico2)
    dico3[(i + 1, list(dico.keys())[i], list(dico2.keys())[i])] = dico[list(dico.keys())[i]] + dico2[list(dico2.keys())[i]]

for key in dico:
    min= None
    neighbour = None
    for key2 in dico:
        if key2 != key:
            if neighbour == None or cosine_distance(key, key2) < min:
                min = cosine_distance(key, key2)
                neighbour = key2
    print("le voisin le plus proche de : \n" + dico[key] + "\nest \n" + dico[neighbour] + "\n avec une distance de " + str(min))

for key in dico2:
    min= None
    neighbour = None
    for key2 in dico2:
        if key2 != key:
            if neighbour == None or cosine_distance(key, key2) < min:
                min = cosine_distance(key, key2)
                neighbour = key2
    print("le voisin le plus proche de : \n" + dico2[key] + "\nest \n" + dico2[neighbour] + "\n avec une distance de " + str(min))



lst = list(dico.keys())
lst2 = list(dico2.keys())
for i in range(len(dico)):
    min = None
    neighbour = None
    for j in range(len(dico)):
        if i != j:
            if neighbour == None or cosine_distance(lst[i], lst[j]) + cosine_distance(lst2[i], lst2[j]) < min :
                min = cosine_distance(lst[i], lst[j]) + cosine_distance(lst2[i], lst2[j])
                neighbour = j
    print("Le voisin le plus proche de " + str(i) + " est " + str(neighbour))

    """