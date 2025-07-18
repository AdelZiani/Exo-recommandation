def nombre_de_lignes(nomdefichier):
    with open(nomdefichier, newline='') as f:
        n = 0
        for line in f:
            n += 1
    return n