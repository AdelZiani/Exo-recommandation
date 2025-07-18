def enumerer2(liste):
    enumeration = [0] * (max(liste) + 1)
    for element in liste:
        enumeration[element] += 1
    return enumeration