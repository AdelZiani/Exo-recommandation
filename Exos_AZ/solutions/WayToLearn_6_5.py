str = 'hello'
n = 1

# Créer une nouvelle chaîne 'str1' qui inclut tous les caractères depuis le début de 'str' jusqu'au caractère à l'index 'n' (non inclus).
str1 = str[:n]

# Créer une nouvelle chaîne 'str2' qui inclut tous les caractères à partir du caractère à l'index 'n+1' jusqu'à la fin de 'str'.
str2 = str[n+1:]

# Afficher le résultat de la concaténation de 'str1' et 'str2', en supprimant le caractère à l'index 'n'.
print(str1 + str2) 