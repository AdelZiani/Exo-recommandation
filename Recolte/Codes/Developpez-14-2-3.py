
# -*- coding : utf8 -*-
"""Somme d'entiers et nombre d'entiers supérieurs à 100."""

# Programme principal =========================================================
somme, nombreTotal, nombreGrands = 0, 0, 0

x = int(input("x (0 pour terminer) ?"))
while x > 0:
    somme += x
    nombreTotal += 1
    if x > 100:
        nombreGrands += 1
    x = int(input("x (0 pour terminer) ?"))

print("\nSomme :", somme)
print(nombreTotal, "valeur(s) en tout, dont", nombreGrands, "supérieure(s) à 100")

