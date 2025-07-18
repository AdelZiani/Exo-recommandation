from random import randint

nbreAtrouver = randint(1,11)
nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
nbreEssai=0
supOuinf=""
if nbreAtrouver==nbreUser:
    print("Trouvé")
else:
    if(nbreUser<nbreAtrouver):
        supOuinf="le chiffre à trouver est supérieur. "
    else:
        supOuinf="le chiffre à trouver est inférieur. "
        
    nbreEssai+=1
    print("NON réessayez, " + supOuinf +" Il vous reste " + str(3-nbreEssai) + " essai(s) ! ")
    nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
    if nbreAtrouver==nbreUser:
        print("Trouvé")
    else:
        if(nbreUser<nbreAtrouver):
            supOuinf="le chiffre à trouver est supérieur. "
        else:
            supOuinf="le chiffre à trouver est inférieur. "
        nbreEssai+=1
        print("NON réessayez, " + supOuinf +" Il vous reste " + str(3-nbreEssai) + " essai(s) ! ")
        nbreUser = int(input("Saisir un entier compris entre 1 et 10 : "))
        if nbreAtrouver==nbreUser:
            print("Trouvé")
        else:
            print("PERDU !")
