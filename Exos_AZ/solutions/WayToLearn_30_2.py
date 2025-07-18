# Créez deux dictionnaires 'x' et 'y' avec des paires clé-valeur.
x = {'A': 1, 'B': 3, 'C': 2}
y = {'A': 1, 'B': 2}
	
# Utiliser les opérations du Set pour trouver les paires clé-valeur communes entre 'x' et 'y'.
# Itérer à travers les paires clé-valeur communes à l'aide d'une boucle for.
for (key, value) in set(x.items()) & set(y.items()):
    # Afficher un message indiquant que la clé et la valeur sont présentes à la fois dans 'x' et 'y'.
    print('%s: %s est présent à la fois dans x et y' % (key, value))