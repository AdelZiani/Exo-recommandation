def cherche(t, element):
    for ligne in t:
        if element in ligne:
            return True
    return False