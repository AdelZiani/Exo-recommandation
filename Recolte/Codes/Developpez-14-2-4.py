
# -*- coding : utf8 -*-
"""Parité."""

# Programme principal =========================================================
n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

if n%2 == 0:
    print(n, "est pair.")
else :
    print(n, "est impair.")

