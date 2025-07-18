
# -*- coding : utf8 -*-
"""Gardien de phare."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def hauteurParcourue(nb, h) :
    print("Pour { :d} marches de { :d} cm, il parcourt { :.2f} m par semaine !"
         .format(nb, h, nb*h*2*5*7/100.0))

# Programme principal =========================================================
nbMarches = int(input("Combien de marches ?"))
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))

hauteurParcourue(nbMarches, hauteurMarche)

