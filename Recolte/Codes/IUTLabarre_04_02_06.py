def indice(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i

    return -1
