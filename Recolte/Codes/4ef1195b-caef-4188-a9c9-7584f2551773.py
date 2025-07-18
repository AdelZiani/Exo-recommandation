def liste_aleatoire_naturels(n, maximum=100):
    liste = list()
    for i in range(n):
        liste.append(randint(0, maximum))
    return liste