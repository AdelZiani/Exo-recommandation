def somme_voisins(i, j, m):
    indices = []
    if i > 0:
        indices.append((i-1, j))
    if i < len(m)-1:
        indices.append((i+1, j))
    if j > 0:
        indices.append((i, j-1))
    if j < len(m[0])-1:
        indices.append((i, j+1))
    somme = 0
    for x, y in indices:
        somme += m[x][y] 
    return somme

def cherche_somme_voisins(t):
    n, m = len(t), len(t[0])
    for i in range(n):
        for j in range(m):
            if t[i][j] == somme_voisins(i, j, t):
                return(i, j)
    return None