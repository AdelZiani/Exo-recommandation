# -*- coding : utf8 -*-
"""Jeu de dés (1)."""

# Programme principal =========================================================
n = int(input("Entrez un entier [2 .. 12] :"))
while not(n >= 2 and n <= 12) :
    n = int(input("Entrez un entier [2 .. 12], s.v.p. :"))

s = 0
for i in range(1, 7) :
    for j in range(1, 7) :
        if i+j == n :
            s += 1

print("Il y a { :d} façon(s) de faire { :d} avec deux dés.".format(s, n))

