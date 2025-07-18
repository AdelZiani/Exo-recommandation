def supprimer_pairs_3(liste):
    for i in range(len(liste)-1, -1, -1):
        if liste[i] % 2 == 0:
            liste.pop(i)