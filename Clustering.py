from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

from modules.clusteringHelp import read_clusters
from modules.models import *

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
    "division operator",
]

phrases = [
    "importation de bibliothèque",
    "initialisation de variable",
    "saisie des données",
    "conversion de type",
    "type flottant",
    "calcul avec PI",
    "division réelle",
    "affichage à l'écran de texte et de valeur de variable",
    "appel de la fonction print",
    "opérateur arithmétique /",
    "opérateur arithmétique *",
    "saisie au clavier",
    "conversion de chaîne en nombre",
    "opérations numériques",
    "importation de bibliothèque",
    "entrée",
    "variables",
    "opérations",
    "opérateur de division",
]

phrases, pred = read_clusters("ClustersEn.txt")

dico = vectorize(SBERT, sentences)
keys = list(dico.keys())
means = KMeans(pred[-1] + 1,n_init=20).fit(keys)
labels = means.labels_
print("Rand Score = " + str(adjusted_rand_score(pred, labels)))
