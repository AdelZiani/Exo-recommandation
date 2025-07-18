
# -*- coding : utf8 -*-
"""Proportion d'une séquence dans une chaîne d'ADN."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valide(seq) :
    """Retourne vrai si la séquence est valide, faux sinon."""
    ret = any(seq)
    for c in seq :
        ret = ret and c in "atgc"
    return ret

def proportion(a, s) :
    """Retourne la proportion de la séquence <s> dans la chaîne <a>."""
    return 100*a.count(s)/len(a)

def saisie(ch) :
    s = input("{ :s} :".format(ch))
    while not valide(s) :
        print("'{ :s}' ne peut contenir que les chaînons 'a', 't', 'g' et 'c'"
              " et ne doit pas être vide".format(ch))
        s = input("{ :s} :".format(ch))
    return s

# Programme principal =========================================================
adn = saisie("chaîne")
seq = saisie("séquence")

print('Il y a { :.2f} % de"{ :s}" dans votre chaîne.'
     .format(proportion(adn, seq), seq))

