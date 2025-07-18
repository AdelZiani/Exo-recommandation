nbrLignes = int(input("Entrer le nombre de lignes: "))

valeur_ascii = 65

for i in range(nbrLignes):
    for j in range(i+1):
        alphabet = chr(valeur_ascii)
        print(alphabet, end=" ")
    
    valeur_ascii += 1
    print()