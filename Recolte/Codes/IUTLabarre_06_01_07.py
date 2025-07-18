def compacte(t1, t2):
    n, m = len(t1), len(t1[0])
    nn, mm = len(t2), len(t2[0])
    if (n, m) != (nn, mm):
        return None
    res = []
    for i in range(n):
        ligne = list()
        for j in range(m):
            ligne.append([t1[i][j], t2[i][j]])
        res.append(ligne)
    return res