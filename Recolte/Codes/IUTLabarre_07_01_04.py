def decoupe_espaces(chaine):
    res = []
    word = ''
    for c in chaine:
        if c != ' ':
            word += c
        else:
            if word != '':
                res.append(word)
            word = ''
    if word != '':
        res.append(word)
    return res
