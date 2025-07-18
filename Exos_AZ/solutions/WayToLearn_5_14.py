n1 = int(input("Entrer le 1er nombre: "))
n2 = int(input("Entrer le 2éme nombre: "))

# chercher la plus petite des deux valeurs n1 et n2
min = n1 if (n1 < n2) else n2

# Itérer de 1 jusqu'à min+1.
for i in range(1, min+1):
    # Vérifier si n1 et n2 sont divisibles par i.
    if (n1 % i == 0 and n2 % i == 0):
        # Mettre à jour le PGCD avec la valeur actuelle de i
        pgcd = i
		
print("PGCD de {0} et {1} = {2}".format(n1, n2, pgcd))