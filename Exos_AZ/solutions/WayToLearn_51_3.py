# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

# Création d'un tableau NumPy 'x' contenant les éléments 1, 4, 6 et 9
x = np.array([1, 4, 6, 9])

# Afficher le Vecteur-1
print("Vecteur-1:", x)

# Générer un tableau NumPy 'y' contenant 4 entiers aléatoires entre 0 et 10 en utilisant np.random.randint()
y = np.random.randint(0, 11, 4)

# Afficher le Vecteur-2
print("Vecteur-2:", y)

# Effectuer une multiplication par éléments entre les tableaux 'x' et 'y' et stocker le résultat dans la variable 'result'.
result = x * y

print("Multiplication des valeurs de deux vecteurs:",result)