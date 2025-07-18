from random import randint

def Exo2Q3():
    nbreAtrouver = randint(1,11)
    nbreUser = input("Saisir un entier compris entre 1 et 10 : ")
    nbreEssai=0
    supOuinf=""
    
    for char in nbreUser:
        if char =='.':    
            print('il faut saisir un entier')
            print ('fin du programme')
            return
    
    nbreUser=int(nbreUser)
    
    if nbreAtrouver==nbreUser:
        print("Trouvé")
    else:
        if(nbreUser<nbreAtrouver):
            supOuinf="le chiffre à trouver est supérieur. "
        else:
            supOuinf="le chiffre à trouver est inférieur. "
            
        nbreEssai+=1
        print("NON réessayez, " + supOuinf +" Il vous reste " + str(3-nbreEssai) + " essai(s) ! ")
        nbreUser = input("Saisir un entier compris entre 1 et 10 : ")
        
        for char in nbreUser:
            if char =='.':    
                print('il faut saisir un entier')
                print ('fin du programme')
                return
        
        nbreUser=int(nbreUser)
        
        if nbreAtrouver==nbreUser:
            print("Trouvé")
        else:
            if(nbreUser<nbreAtrouver):
                supOuinf="le chiffre à trouver est supérieur. "
            else:
                supOuinf="le chiffre à trouver est inférieur. "
            nbreEssai+=1
            print("NON réessayez, " + supOuinf +" Il vous reste " + str(3-nbreEssai) + " essai(s) ! ")
            nbreUser = input("Saisir un entier compris entre 1 et 10 : ")
            
            for char in nbreUser:
                if char =='.':    
                    print('il faut saisir un entier')
                    print ('fin du programme')
                    return
            
            nbreUser=int(nbreUser)
            
            if nbreAtrouver==nbreUser:
                print("Trouvé")
            else:
                print("PERDU !")