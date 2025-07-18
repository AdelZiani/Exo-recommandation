def grille_valide_aleatoire():
    # On a une matrice valide de base
    grille = [
        [1, 2, 3, 7, 8, 9, 4, 5, 6],
        [4, 5, 6, 1, 2, 3, 7, 8, 9],
        [7, 8, 9, 4, 5, 6, 1, 2, 3],
        [2, 3, 1, 8, 9, 7, 5, 6, 4],
        [5, 6, 4, 2, 3, 1, 8, 9, 7],
        [8, 9, 7, 5, 6, 4, 2, 3, 1],
        [3, 1, 2, 9, 7, 8, 6, 4, 5],
        [6, 4, 5, 3, 1, 2, 9, 7, 8],
        [9, 7, 8, 6, 4, 5, 3, 1, 2]
    ]

    # Appliquer un décalage modulaire aléatoire
    decalage = randint(1, 8)
    grille = [[(case + decalage) % 9 + 1 for case in ligne] for ligne in grille]

    # Appliquer une symétrie aléatoire (horizontale, verticale ou diagonale)
    symmetrie = choice(['horizontale', 'verticale', 'diagonale'])
    if symmetrie == 'horizontale':
        grille = [ligne[::-1] for ligne in grille]
    elif symmetrie == 'verticale':
        grille = [list(ligne) for ligne in zip(*grille[::-1])]
    else:
        grille = [list(ligne) for ligne in zip(*[list(reversed(ligne)) for ligne in zip(*grille)])]

    return grille