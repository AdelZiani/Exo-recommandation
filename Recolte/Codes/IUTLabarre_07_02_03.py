def binaire_vers_decimal(b):
    puissance = 1
    resultat = 0
    for i in range(len(b) - 1, -1, -1):
        assert (b[i] == '0' or b[i] == '1')
        resultat += int(b[i]) * puissance
        puissance *= 2
    return resultat
