def liste_aleatoire_triee(n, maximum=100, pas=10):
    if not n:
        return []
    
    retval = [randint(0, maximum)]
    for i in range(1, n):
        retval.append(randint(retval[-1], retval[i-1] + pas))
    return retval