def enumerer1(liste):
    enumeration = [0] * (max(liste) + 1)
    for i in range(len(enumeration)):
        enumeration[i] = liste.count(i)
    return enumeration