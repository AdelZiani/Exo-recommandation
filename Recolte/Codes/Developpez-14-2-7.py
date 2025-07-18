
# -*- coding : utf8 -*-
"""Approximation de 'e'."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fact(n) :
    r = 1
    for i in range(1, n+1) :
        r *= i
    return r

# Programme principal =========================================================
n = int(input("n ?"))
exp = 0.0
for i in range(n) :
    exp = exp + 1.0/fact(i)

print("Approximation de 'e' : { :.3f}".format(exp))

