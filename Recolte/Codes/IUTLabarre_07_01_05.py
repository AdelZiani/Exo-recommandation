import string

def decoupe_seps(chaine, seps):
    res = []
    word = ''
    for c in chaine:
        if not (c in seps):
            word += c
        else:
            if word != '':
                res.append(word)
            word = ''
    if word != '':
        res.append(word)
    return res


# attention, dans le doctest, decoupe("aaa b   cc \\naaa ") correspond à l'appel de decoupe("aaa b   cc \naaa ")
def decoupe(chaine):
    return decoupe_seps(chaine, string.whitespace)
