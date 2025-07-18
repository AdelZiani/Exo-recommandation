# -*- coding : utf8 -*-
"""Nombres romains (version 2)."""

# globales ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CODE = zip(
    [1000,  900, 500,  400, 100,  90,   50,  40,   10,  9,    5,    4,   1],
    [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
)

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def decToRoman(num) :
    res = []
    for d, r in CODE :
        while num >= d :
            res.append(r)
            num -= d
    return ''.join(res)

# Programme principal =========================================================
for i in range(1, 4000) :
    print(i, decToRoman(i))

