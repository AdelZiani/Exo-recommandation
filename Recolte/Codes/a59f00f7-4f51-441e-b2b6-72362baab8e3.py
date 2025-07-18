def multiplications(n):
    produit = 1
    for i in range(n):
        produit *= random() + 0.0000000001  # rajout pour éviter les zéros

    return produit