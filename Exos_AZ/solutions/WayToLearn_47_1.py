# Définir une fonction lambda 'is_num' qui vérifie si une chaîne donnée 's' représente un nombre
# Elle supprime d'abord la première virgule de la chaîne en utilisant 'replace()',
# puis vérifie si la chaîne résultante est composée de chiffres en utilisant 'isdigit()'
is_num = lambda s: s.replace('.', '', 1).isdigit()

# Vérifier si les chaînes données sont numériques en utilisant la fonction lambda 'is_num'
print(is_num('15'))
print(is_num('1.5'))
print(is_num('001')) 
print(is_num('F001'))