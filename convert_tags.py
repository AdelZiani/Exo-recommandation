from modules.models import CODEBERT, vectorize
import csv
import sys
import os



#args[1] = le fichier avec tout les tags
#args[2] = le repertoire avec enonces, solutions et tags 
#créé un fichier data.csv avec les solutions vectorisé avec codeBERT et les tags sous forme de vecteurs binaire

#  Tags folder
args = sys.argv

if len(args) <3:
    print("pas assez d'arguments")
    exit()
list_tags = []
tags = args[1]
tags = open(tags,"r")
assignations = os.listdir(args[2] +"/tags")
solutions = os.listdir(args[2] +"/solutions")
print(type(assignations[0]))
print(len(solutions))
for line in tags.readlines():
    if not line.startswith("#"):
        list_tags.append(line.split("#")[0])
print(len(list_tags))

with open('data.csv',  mode='w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["Solution", "Tags"])
    for elem in assignations:
        f = open(args[2]+ "/tags/" + elem, "r")
        fsol = open(args[2] + "/solutions/" + elem.replace(".tag",".py"), "r")
        sol = fsol.read()
        fsol.close()
        dico = vectorize(CODEBERT, [sol])
        print(len(dico.keys()))
        print(list(dico.keys())[0])
        lines = f.readlines()
        tags_bin = [0] * len(list_tags)
        for line in lines:
            tags_bin[list_tags.index(line.removesuffix("\n"))] = 1
        spamwriter.writerow([list(dico.keys())[0], tags_bin])
    print(tags_bin)
    f.close()
