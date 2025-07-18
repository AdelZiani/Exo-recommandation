def combine(lst1, lst2):
    res = []
    n = min(len(lst1), len(lst2))
    for i in range(n):
        res.append(lst1[i])
        res.append(lst2[i])
    for j in range(n, len(lst1)):
        res.append(lst1[j])
    for j in range(n, len(lst2)):
        res.append(lst2[j])
    return res