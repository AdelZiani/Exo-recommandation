def supprimer_pairs_1(liste):
    i = 0
    taille = len(liste)
    while i < taille:
        if liste[i] % 2 == 0:
            liste.pop(i)
            taille -= 1
        else:
            i += 1