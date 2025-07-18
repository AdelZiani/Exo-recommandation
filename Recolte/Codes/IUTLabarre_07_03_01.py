def motif_position(chaine, i, motif):
    j = i
    if i < 0 or i > len(chaine) - len(motif):
        return False
    for c in motif:
        if chaine[j] != c:
            return False
        j += 1
    return True


def est_motif(chaine, motif):
    for i in range(len(chaine) - len(motif) + 1):
        if motif_position(chaine, i, motif):
            return True
    return False