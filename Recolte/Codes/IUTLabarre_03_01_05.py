n = int(input("Entrez un entier n positif: "))
print("\nVoici les n premiers multiples de 3 dans l'ordre décroissant: ")
for i in range(n - 1, -1, -1):
    print(3 * i, end=' ')