# -*- coding : utf8 -*-
"""Amplitude et moyenne d'une liste de flottants."""

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from random import seed, random

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listAleaFloat(n) :
    "Retourne une liste de <n> flottants aléatoires"
    return [random() for i in range(n)]

# Programme principal =========================================================
n = int(input("Entrez un entier [2 .. 100] :"))
while not(n >= 2 and n <= 100) :
    n = int(input("Entrez un entier [2 .. 100], s.v.p. :"))

seed() # initialise le générateur de nombres aléatoires
t = listAleaFloat(n) # construction de la liste

print("Amplitude : { :.2f}".format(max(t) - min(t)))
print("Moyenne : { :.2f}".format(sum(t)/n))

