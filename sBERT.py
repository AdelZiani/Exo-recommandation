from modules.clusteringHelp import DBScan, kmeans, hierarchical_clustering
from modules.models import *
# Sentences we want sentence embeddings for
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

dico = vectorize(CAMEMBERT, phrases)


print("\nkmeans +++++++++++++++++++++++++++++++++++++++++++++\n")
kmeans(5, dico)
print("\nhierarchical ++++++++++++++++++++++++++++++++++++++++++++\n")
hierarchical_clustering(5, dico)
print("\nDBSCAN ++++++++++++++++++++++++++++++++++++++++++\n")
DBScan(dico)