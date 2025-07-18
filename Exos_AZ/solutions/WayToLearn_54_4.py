# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

tab = np.arange(10, 21)

print("Tableau original:")
print(tab)

print("Tableau inversé:")
tab = tab[::-1]
print(tab)