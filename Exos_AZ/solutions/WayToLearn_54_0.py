# Importer la bibliothèque NumPy avec l'alias 'np'.
import numpy as np

# Création d'une valeur numpy.float32 'x' initialisée à 0
x = np.float32(0)

# Affichage du type de 'x'
print(type(x))

# Extraction de la valeur float Python de numpy.float32 'x' à l'aide de la méthode item()
py = x.item()

# Affichage du type de la valeur flottante Python extraite.
print(type(py))