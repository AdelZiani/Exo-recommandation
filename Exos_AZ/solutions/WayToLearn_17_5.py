# Importer la classe "Counter" du module "collections"
from collections import Counter

# Définir deux listes 'color1' et 'color2' contenant des noms de couleurs
color1 = ["orange", "green", "white"]
color2 = ["black", "yellow", "green"]

# Créer des objets Counter 'counter1' et 'counter2' pour chaque liste afin 
# de compter les occurrences des noms de couleurs.
counter1 = Counter(color1)
counter2 = Counter(color2)

# Afficher les éléments qui sont dans 'counter1' mais pas 
# dans 'counter2' (Color1 - Color2)
print("Color1 - Color2: ", list(counter1 - counter2))

# Afficher les éléments qui se trouvent dans 'counter2' mais 
# pas dans 'counter1' (Color2 - Color1)
print("Color2 - Color1: ", list(counter2 - counter1))