import pandas as pd
import numpy as np
from modules.models import *



zi = 0
lst = ["Labarre", "Git", "Developpez", "Platon"]
Tags = open("Tags.txt", "r")
tags = Tags.read().split(",")
allTags = []
df = pd.DataFrame(columns=["code", "tag"])
for elem in lst:
    print(elem)
    f = open("Tags_"+ elem +".tsv",'r')
    f.readline()


    line = None
    line = f.readline()
    while line != "":
        line = line.split("\t")
        name = line[1]
        code = open("Codes/" +name, "r")
        vector = vectorize(CODEBERT, [code.read()])
        for key in vector:
            vec = key
        line = line[2]
        tagsline = []
        while line.startswith(","):
            line = line.removeprefix(",")
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].removeprefix(" ")
            line[i] = line[i].removesuffix(" ")
            line[i] = line[i].removeprefix("\n")
            line[i] = line[i].removesuffix("\n")
        for elem in tags:
            if elem in line:
                tagsline.append(1)
                zi +=1
                print("ziiii  ", zi)
            else:
                tagsline.append(0)
        dico = {"code" : vec, "tag" : tagsline}
        nouvelle_ligne = pd.DataFrame([dico])
        df = pd.concat([df, nouvelle_ligne], ignore_index=True)
        allTags.extend(line)
        line = f.readline()
print(len(allTags))
df.to_csv("donnees.csv", index=False, encoding='utf-8')
for tag in allTags:
    if allTags.count(tag) > 20:
        print(allTags.count(tag))
        print(tag)
allTags = list(set(allTags))
print(len(allTags))
