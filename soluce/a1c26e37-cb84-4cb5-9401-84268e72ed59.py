def supprimer_pairs_2(liste):
    liste_auxiliaire = list()
    for element in liste:
        if element % 2 != 0:
            liste_auxiliaire.append(element)
            
    # On écrase la liste si le résultat est diffère de la liste initiale
    if len(liste) != len(liste_auxiliaire):
        liste[:] = liste_auxiliaire