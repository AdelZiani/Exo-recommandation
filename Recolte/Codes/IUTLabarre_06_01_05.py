def somme_colonnes(t):
    if not t:
        return []
    n = len(t[0])
    res = [0] * n
    for line in t:
        for j in range(n):
            res[j] += line[j]
    return res