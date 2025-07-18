# Définir deux listes contenant des nombres entiers
liste1 = [10, 20, 30]
liste2 = [40, 50, 60]

# Utilisez le découpage de liste pour insérer les éléments de 'liste2' 
# au début de 'liste1' en définissant 'liste1[:0] = liste2'.
liste1[:0] = liste2

# Les éléments de la 'liste2' sont ainsi ajoutés au début de la 'liste1'
print(liste1)