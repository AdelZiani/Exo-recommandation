# -*- coding : utf8 -*-
"""Nombres romains (version 1)."""

# Programme principal =========================================================
n = int(input('Entrez un entier [1 .. 4000[ : '))

while not(n >= 1 and n < 4000) :
    n = int(input('Entrez un entier [1 .. 4000[, s.v.p. : '))

s = "" # Chaîne résultante

while n >= 1000:
    s += "M"
    n -= 1000
if n >= 900:
    s += "CM"
    n -= 900
if n >= 500:
    s += "D"
    n -= 500
if n >= 400:
    s += "CD"
    n -= 400

while n >= 100:
    s += "C"
    n -= 100
if n >= 90:
    s += "XC"
    n -= 90
if n >= 50:
    s += "L"
    n -= 50
if n >= 40:
    s += "XL"
    n -= 40
while n >= 10:
    s += "X"
    n -= 10
if n >= 9:
    s += "IX"
    n -= 9
if n >= 5:
    s += "V"
    n -= 5
if n >= 4:
    s += "IV"
    n -= 4
while n >= 1:
    s += "I"
    n -= 1

print("En romain :", s)

