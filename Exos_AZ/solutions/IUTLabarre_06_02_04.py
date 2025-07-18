def decoupage_croissant(lst):
    if not lst:
        return []
    resultat = [ [lst[0]] ]
    i_dst = 0 # l'indice de la sous-liste de destination
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            resultat.append([])
            i_dst += 1
        resultat[i_dst].append(lst[i])
    return resultat