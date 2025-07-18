# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

# Création d'un tableau NumPy 'tab' contenant les valeurs d'une matrice 3x3
tab = np.array([[5, 3, 7],
                [3, 8, 6],
                [1, 2, 9]])

print("Tableau original:")
print(tab)

n = 8
r = 5

print("\nRemplacer les éléments qui sont égaux à", n, "par", r)
print(np.where(tab == n, r, tab))

print("\nRemplacer les éléments qui sont inférieurs à", n, "par", r)
print(np.where(tab < n, r, tab))

print("\nRemplacer les éléments qui sont supérieurs à", n, "par", r)
print(np.where(tab > n, r, tab))