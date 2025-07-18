def nb_occurrences(n, l):
    nb = 0
    for e in l:
        if e == n:
            nb += 1
    return nb