
# -*- coding : utf8 -*-
"""Echanges."""

# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from random import seed, randint

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listAleaInt(n, a, b) :
    """Retourne une liste de <n> entiers aléatoires dans [<a> .. <b>]."""
    return [randint(a, b) for i in range(n)]

# Programme principal =========================================================
seed() # initialise le générateur de nombres aléatoires
t = listAleaInt(100, 2, 125) # construction de la liste

iMin = t.index(min(t)) # calcule l'index du minimum de la liste

print("Avant échange :")
print("\tt[0] =", t[0], "\tt[iMin] =", t[iMin])
t[0], t[iMin] = t[iMin], t[0] # échange
print("Apres échange :")
print("\tt[0] =", t[0], "\tt[iMin] =", t[iMin])

