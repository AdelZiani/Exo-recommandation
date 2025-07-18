liste = ["Hello", "waytolearnx", "PHP", "Bob"]

#Utilisez la fonction filter pour extraire les lettres majuscules
maj_letters = list(filter(lambda char: char.isupper(), ''.join(liste)))

print("\nExtraire toutes les lettres majuscules:")
print(maj_letters)