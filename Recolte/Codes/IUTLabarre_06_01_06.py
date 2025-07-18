def copie(t):
    m = list()
    for ligne in t:
        nouvelle_ligne = list()
        for x in ligne:
            nouvelle_ligne.append(x)
        m.append(nouvelle_ligne)
    return m

def annule_diagonales(t):
    n, m = len(t), len(t[0])
    if n != m:
        return t
    m = copie(t)
    for i in range(n):
        m[i][i] = 0
        m[i][n-1-i] = 0
    return m