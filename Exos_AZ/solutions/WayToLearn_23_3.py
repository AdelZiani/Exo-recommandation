liste = ['8', '-15', '9', '0', '1']

print("Liste originale:",liste)

# Convertir chaque chaîne numérique en un entier et stocker le résultat dans 'result'
result = [int(x) for x in liste]

# Trier la liste des résultats par ordre croissant
result.sort()
	
print("Liste triée:", result)