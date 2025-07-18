def additions_int(n, b=1000):
    somme = 0
    for i in range(n):
        somme += randint(1, b)

    return somme