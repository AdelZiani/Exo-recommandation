from random import randint

nbreAtrouver = randint(1,11)

nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
nbreEssai=0
if nbreAtrouver==nbreUser:
    print("Trouvé")
else:
    nbreEssai+=1
    print("NON réessayez, reste " + str(3-nbreEssai) + " essai(s) ! ")
    nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
    if nbreAtrouver==nbreUser:
        print("Trouvé")
    else:
        nbreEssai+=1
        print("NON réessayez, reste " + str(3-nbreEssai) + " essai(s) ! ")
        nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
        if nbreAtrouver==nbreUser:
            print("Trouvé")
        else:
            print("PERDU !")