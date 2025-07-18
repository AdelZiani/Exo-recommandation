# -*- coding : utf8 -*-
"""Jeu de dés (2)."""

# Programme principal =========================================================
n = int(input("Entrez un entier [3 .. 18] :"))
while not(n >= 3 and n <= 18) :
    n = int(input("Entrez un entier [3 .. 18], s.v.p. :"))

s = 0
for i in range(1, 7) :
    for j in range(1, 7) :
        for k in range(1, 7) :
            if i+j+k == n :
                s += 1

print("Il y a { :d} façon(s) de faire { :d} avec trois dés.".format(s, n))

