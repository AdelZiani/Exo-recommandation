string = input("Entrez une chaine de caractères: ")

voyelles = "aeiouyAEIOUY"
for letter in string:
    if letter in voyelles:
        print("e", end="")
    else:
        print(letter, end='')