import matplotlib.pyplot as plt
import numpy as np
import os, sys
import zss
import ast
from Comparaison_exercices import solution

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../AST')))

from models import *
from vectors_operations import cosine_distance
import ZSS
dataframe = open("df", "w")

def cleanGit(code):
    while code.endswith("\n") or code.startswith("\n"):
        code= code.removesuffix("\n").removeprefix("\n")
    code = code.removeprefix("```python").removesuffix("```")
    return code

              # Valeurs de sin(x)

lst1 = []
lst2 = []

dico2 = vectorize(CODEBERT, solution())


for key in dico2:
    min= None
    neighbour = None
    for key2 in dico2:
        distancecodeBert = cosine_distance(key, key2)
        distanceZSS = zss.simple_distance(ZSS.convert_ast(ast.parse(cleanGit(dico2[key]))), ZSS.convert_ast(ast.parse(cleanGit(dico2[key2]))))
        lst1.append(distancecodeBert)
        #print(cleanGit(dico2[key]), "###################################################################################################")
        #print(cleanGit(dico2[key2]), "###################################################################################################")
        lst2.append(distanceZSS)
        dataframe.write(str(distanceZSS) + ","+ str(distancecodeBert) + "\n" +dico2[key] + "\n ############################################# \n"+dico2[key2] + "\n" )
        #neighbour = key2

dataframe.close()

# Création du graphe
plt.figure(figsize=(8, 5))       # Taille de la figure
plt.scatter(np.array(lst1), np.array(lst2), color='blue', s=10, marker='o')  # Points non reliés

# Ajout de titres et légendes
plt.title('Graphe de distances de codes')
plt.xlabel('codeBERT distance')
plt.ylabel('ast distance')
plt.legend()
plt.grid(True)

# Affichage du graphe
plt.show()