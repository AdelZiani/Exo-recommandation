from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM

import math

import numpy as np

from modules.clusteringHelp import DBScan, kmeans, hierarchical_clustering

from modules.models import *

import torch
from modules.vectors_operations import cosine_distance

model = AutoModel.from_pretrained(CAMEMBERT)
tokenizer = AutoTokenizer.from_pretrained(CAMEMBERT)

sentences =[
    "library import",
    "variable initialization",
    "data input",
    "casting",
    "float type",
    "calculation with PI",
    "real division",
    "screen display of text and variable value",
    "print function call",
    "arithmetic operator /",
    "arithmetic operator *",
    "keyboard input",
    "string to number conversion",
    "numeric operations",
    "library import",
    "input",
    "variables",
    "operations",
    "division operator"
]

phrases = [
    "input",
    "variables",
    "operations",
    "cast",
    "import",
    "entrées clavier",
    "conversion de chaines de caractères",
    "opérations numériques",
    "import de bibliothèque",
    "initialisation de variable",
    "input de données",
    "type float",
    "calcul avec PI",
    "division réel",
    "affichage écran texte et valeur d'une variable",
    "appel fonction print",
    "opérateur arithmétique /",
    "opérateur arithmétique *"
]

encoded_input = tokenizer(phrases, padding=True, truncation=True, return_tensors='pt')
print("")
print(encoded_input.tokens())


with torch.no_grad():
    model_output = model(**encoded_input)


"""
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

"""

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
                vectors.append(outputs[i].detach().numpy().tolist())
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


print(encoded_input.tokens())
tagsnew = define_tags(encoded_input.tokens(), model_output[0][0])





print_values(tagsnew)


print("\nkmeans +++++++++++++++++++++++++++++++++++++++++++++\n")
kmeans(3, tagsnew)
print("\nhierarchical ++++++++++++++++++++++++++++++++++++++++++++\n")
hierarchical_clustering(3, tagsnew)
print("\nDBSCAN ++++++++++++++++++++++++++++++++++++++++++\n")
DBScan(tagsnew)