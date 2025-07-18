def motif_position(chaine, i, motif):
    j = i
    if i < 0 or i > len(chaine) - len(motif):
        return False
    for c in motif:
        if chaine[j] != c:
            return False
        j += 1
    return True


def nombre_motif(chaine, motif):
    count = 0
    for i in range(len(chaine) - len(motif) + 1):
        if motif_position(chaine, i, motif):
            count += 1
    return count
