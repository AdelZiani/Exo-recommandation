# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])

# Transformer le tableau 'x' en une matrice 3x2 et l'affecter à la variable 'y'.
y = np.reshape(x, (3, 2))
print("Reshape 3x2:")
print(y) 

# Transformer le tableau 'x' en une matrice 2x3 et l'affecter à la variable 'z'.
z = np.reshape(x, (2, 3))
print("Reshape 2x3:")
print(z)