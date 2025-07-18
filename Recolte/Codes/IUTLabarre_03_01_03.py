n = int(input("Entrez un entier n positif: "))
print("\nVoici parmi les n premiers nombres ceux qui sont divisibles par 3 mais pas par 5: ")
for i in range(1, n):
    if not i % 3 and i % 5:
        print(i, end=' ')