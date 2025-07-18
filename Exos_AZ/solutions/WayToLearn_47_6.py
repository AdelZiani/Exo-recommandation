names = ['Alex', 'Bob', 'Olivier', 'Ali', 'Emily']

print("Liste original:")
print(names) 

# Utiliser la fonction 'filter()' avec une fonction lambda pour filtrer les jours avec une longueur de 3 caractères
# La fonction lambda vérifie la longueur de chaque nom et ne garde que les jours ayant une longueur de 3 caractères.
# Les chaînes vides ('') sont filtrées pour ne garder que les jours avec une longueur de 3 caractères
names = filter(lambda name: name if len(name) == 3 else '', names)

print("\nNoms ayant une longueur de 3 caractères:")
# Parcourez les jours filtrés et affichez chaque nom ayant une longueur de 3 caractères.
for i in names:
    print(i)