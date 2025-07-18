nbrLignes = int(input("Entrer le nombre de lignes: "))

coef = 1

for i in range(1, nbrLignes+1):
    for espace in range(1, nbrLignes-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()