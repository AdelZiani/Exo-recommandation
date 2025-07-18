def matrice_carree_aleatoire(n):
    matrice = []
    for i in range(n):
        matrice.append([randint(1,9) for i in range(n)])
    return matrice