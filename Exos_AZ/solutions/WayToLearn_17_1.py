# Créer une liste imbriquée 'l' à l'aide d'une compréhension de liste
# Cette compréhension de liste génère une matrice 4x4 dont les éléments sont calculés à l'aide de la formule 4*i + j
l = [[4*i + j for j in range(1, 5)] for i in range(4)]

# Afficher la matrice 4x4 résultante 'l'
print(l)