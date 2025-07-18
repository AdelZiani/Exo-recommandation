
# -*- coding : utf8 -*-
"""Permis de chasse."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def permisSup(p, c, v, a) :
    pointsPerdus = p + 3*c + 5*v + 10*a
    nbrePermis = pointsPerdus/100.0
    return 200*nbrePermis

# Programme principal =========================================================
poules = int(input("Combien de poules ?"))
chiens = int(input("Combien de chiens ?"))
vaches = int(input("Combien de vaches ?"))
amis = int(input("Combien d'amis ?"))

payer = permisSup(poules, chiens, vaches, amis)

print("\nA payer :", end=' ')
if payer == 0:
    print("rien à payer")
else :
    print(payer, "euros")

