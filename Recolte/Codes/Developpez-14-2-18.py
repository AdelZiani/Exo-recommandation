# -*- coding : utf8 -*-
"""Liste d'entiers différents (seconde version)."""

avant = [20, 10, 5, 45, 68, 5, 1, 2]
apres = list(set(avant))

if len(avant) == len(apres) :
    print("\nTous les éléments sont distincts.")
else :
    print("\nAu moins une valeur est répétée.")
