
# -*- coding : utf8 -*-
"""Min, max et moyenne d'une liste d'entiers."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def minMaxMoy(liste) :
    """Renvoie le min, le max et la moyenne de la liste."""
    min, max, som = liste[0], liste[0], float(liste[0])
    for i in liste[1:]:
        if i < min :
            min = i
        if i > max :
            max = i
        som += i
    return (min, max, som/len(liste))

# Programme principal =========================================================
lp = [10, 18, 14, 20, 12, 16]

print("liste =", lp)
l = minMaxMoy(lp)
print("min : {0[0]}, max : {0[1]}, moy : {0[2]}".format(l))

