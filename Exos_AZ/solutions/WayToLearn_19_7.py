liste = [14.4, 2.0, 11.0, -18.22, 19.2, -5.2, 16.5]

print("Liste originale:", liste)

# Utilisez la fonction "map" pour arrondir chaque nombre dans "liste" et stockez le résultat dans nbrs
nbrs = list(map(round, liste))

# Afficher la valeur minimale de la liste "nbrs"
print("Minimum value: ", min(nbrs))

# Afficher la valeur maximale de la liste "nbrs"
print("Maximum value: ", max(nbrs))

# Créer un Set à partir de 'nbrs' pour supprimer les doublons, puis trier et multiplier chaque valeur par 5
# Stocker le résultat dans 'nbrs'
nbrs = sorted(map(lambda n: n * 5, set(nbrs)))

print("Résultat:")

# Parcourir la liste 'nbrs' et afficher chaque valeur séparée par un espace.
for i in nbrs:
    print(i, end=' ') 