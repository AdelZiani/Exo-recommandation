def decoupe_simple(chaine):
    res = []
    word = ''
    for c in chaine:
        if c != ' ':
            word += c
        else:
            res.append(word)
            word = ''
    res.append(word)
    return res