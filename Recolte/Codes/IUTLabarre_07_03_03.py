def motif_position(chaine, i, motif):
    j = i
    if i < 0 or i > len(chaine) - len(motif):
        return False
    for c in motif:
        if chaine[j] != c:
            return False
        j += 1
    return True

def remplace_motif(chaine, motif1, motif2):
    res = ""
    i = 0
    while i < len(chaine):
        if motif_position(chaine, i, motif1):
            res += motif2
            i += len(motif1)
        else:
            res += chaine[i]
            i += 1
    return res


def remplace_caractere(chaine, car, motif):
    return remplace_motif(chaine, car, motif)