liste = [1, 2, 3, 4, 5]

# Définir la plage "m" et "n"
m = 1
n = 3

print("Liste originale:",liste)

# Initialiser 's' pour stocker la somme de l'intervalle spécifié
s = 0
    
# Parcourir la liste de l'index "m" à l'index "n"
for i in range(m, n+1, 1):
    # Ajouter la valeur de l'index actuel "i" à "s"
    s += liste[i]
    
print("Somme de la plage spécifiée:",s) 