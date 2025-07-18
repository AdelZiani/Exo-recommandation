import zss
import ast
import csv
import sys
import os
from modules.models import CODEBERT, vectorize
from modules.vectors_operations import cosine_distance
code = """
def range_append(n):
    lst=[]
    i = 1
    while i < n + 1:
        lst.append(i)
        i += 1
    return lst
"""

"""
def range_insert(n):
    lst=[]
    for i in range(n,0,-1):
        # insertion en fin de liste 
        lst.insert(0, i)
    return lst
"""

code2 ="""
def range_append(n):
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    return lst
"""

args = sys.argv



def get_distances():
    solutions = os.listdir(args[1] +"/solutions")
    enonces = os.listdir(args[1] +"/enonces")
    sentences = []
    i = []
    for elem in solutions:
        sentences.append(open(args[1] + "/solutions/" + elem, "r").read()) 
        i.append(elem)
    dico = vectorize(CODEBERT, sentences)
    keys = list(dico.keys())
    with open('neighbour_BERT.csv',  mode='w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["Enonce1", "Solution1", "Enonce2", "Solution2", "Score"])
        for elem in keys:
            for elem2 in keys:
                dist = cosine_distance(elem, elem2)
                spamwriter.writerow([open(args[1] + "/enonces/" + i[sentences.index(dico[elem])].replace(".py", ".txt").replace("soluce", "énoncé"), "r").read(), dico[elem], open(args[1] + "/enonces/" + i[sentences.index(dico[elem])].replace(".py", ".txt").replace("soluce", "énoncé"), "r").read(), dico[elem2], dist])



                

get_distances()

"""
for i in range(1,100):
    dico = {}
    temoin = open("solutions/Github" + str(i) + ".py")
    temoin = temoin.read().removeprefix("```python").removesuffix("```")
    while temoin.endswith("\n") or temoin.startswith("\n"):
        temoin= temoin.removesuffix("\n").removeprefix("\n")
    temoin = temoin.removeprefix("```python").removesuffix("```")
    print("le code temoin : \n", temoin, "\n\n son ast: \n\n")
    print(ast.dump(ast.parse(temoin), indent=4)) 
    # Recherche de l'ast le plus proche
    for j in range(1, 100):
        f = open("solutions/Github" + str(j) + ".py")
        code = f.read()
        while code.endswith("\n") or code.startswith("\n"):
            code = code.removesuffix("\n").removeprefix("\n")
        code = code.removeprefix("```python").removesuffix("```")
        tree = ast.parse(code)
        dico[code] = zsrange_append',
            args=argumentss.simple_distance(convert_ast(ast.parse(temoin)), convert_ast(tree))
    plus_petits = sorted(dico.items(), key=lambda x: x[1])[:3]
    cles_plus_petites = [cle for cle, val in plus_petits]
    for elem in cles_plus_petites:
        print("voisin : \n", elem)
    print("------------------------------------------------------------------------------------------------------------------------")"""

"""
This function return 5 
"""