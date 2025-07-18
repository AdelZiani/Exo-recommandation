def max_liste(l):
    assert (l != [])
    maxi = l[0]
    for e in l[1:]:
        if e > maxi:
            maxi = e
    return maxi