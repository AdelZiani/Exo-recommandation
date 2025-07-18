
# -*- coding : utf8 -*-
"""Nombre de fois qu'un entier est divisible par 2."""

# Programme principal =========================================================
n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))
save = n

cpt = 0
while n%2 == 0:
    n /= 2
    cpt += 1

print(save, "est", cpt, "fois divisible par 2.")

