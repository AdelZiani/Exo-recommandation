# Définir une liste contenant des entiers
liste = [1, 2, 3, 4]

# Utiliser une liste de compréhension pour créer une nouvelle liste 
# de chaînes, où chaque chaîne est formée en ajoutant l'index 
# (formaté comme une chaîne) à la chaîne 'id'. Cela génère effectivement 
# une liste de chaînes avec des éléments tels que 'id1', 'id2', 'id3', 'id4'.
my_list = ['id{0}'.format(i) for i in liste]

# Afficher la nouvelle liste "ma_liste" contenant les chaînes de caractères formatées
print(my_list)