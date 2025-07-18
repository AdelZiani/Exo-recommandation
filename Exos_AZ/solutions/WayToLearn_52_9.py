# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

tab = np.array([[2.55, 5.39, 6.89],
              [4.83, 6.13, 7.88],
              [2.32, 3.78, 9.14]])
print("Tableau original:")
print(tab)
print("\nNouveau tableau de même forme/type, rempli par 0:")
print(np.zeros_like(tab))