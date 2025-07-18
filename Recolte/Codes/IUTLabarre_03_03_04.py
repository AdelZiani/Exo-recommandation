string = input("Entrez une chaine de caractères: ")

i = 1
for letter in string:
    if i % 2:
        print(letter, end='')
    i += 1