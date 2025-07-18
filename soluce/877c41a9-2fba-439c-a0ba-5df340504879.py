def multiplications_int(n, b=1000):
    produit = 1
    for i in range(n):
        produit *= randint(1, b)

    return produit