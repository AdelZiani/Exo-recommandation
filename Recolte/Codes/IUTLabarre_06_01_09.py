
def copie(t):
    m = list()
    for ligne in t:
        nouvelle_ligne = list()
        for x in ligne:
            nouvelle_ligne.append(x)
        m.append(nouvelle_ligne)
    return m

def decalage_cyclique(t):
    n, m = len(t), len(t[0])
    res = copie(t)
    for i in range(m-1):
        res[0][i+1] = t[0][i]
        res[n-1][i] = t[n-1][i+1]
    for j in range(n-1):
        res[j+1][m-1] = t[j][m-1]
        res[j][0] = t[j+1][0]
    return res