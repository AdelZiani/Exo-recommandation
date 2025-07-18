
# -*- coding : utf8 -*-
"""Histoire de train."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def tchacatchac(v) :
    """Affiche l'heure du drame."""
    heure = 9 + int(170/v)
    minute = (60 * 170 / v) % 60
    print("A { :>3} km/h, je me fais déchiqueter à { :>2} h { :.2f} min."
         .format(v, heure, minute))

# Programme principal =========================================================
i = 100
while i <= 300:
    tchacatchac(i)
    i += 10

