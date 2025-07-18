def croissant_depuis(i, l):
    if not l:
        return []
    res = [l[i]]
    for j in range(i+1, len(l)):
        if l[j-1] > l[j]:
            break
        res.append(l[j])
    return res

def debut_croissant(lst):
    return croissant_depuis(0, lst)