def separe(lst):
    l0 = []
    l1 = []
    n = len(lst)
    if n <= 1:
        return lst, []
    for i in range(0, n-1, 2):
        l0.append(lst[i])
        l1.append(lst[i+1])
    if i+2 != n:
        l0.append(lst[n-1])
    return [l0, l1]