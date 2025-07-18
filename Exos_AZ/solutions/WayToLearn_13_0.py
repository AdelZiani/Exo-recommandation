def lire_fichier(nom_fichier):
        fichier = open(nom_fichier)
        print(fichier.read())

lire_fichier('test.txt')