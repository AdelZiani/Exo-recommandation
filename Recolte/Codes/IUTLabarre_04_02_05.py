def singletons(l):
    sing = []
    for e in l:
        if not e in sing:
            sing.append(e)
    return sing
