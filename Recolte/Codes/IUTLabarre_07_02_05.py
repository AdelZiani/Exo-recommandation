

def nombre_vers_lettre(nombre):
    assert (0 <= nombre < 16)
    if nombre in range(10):
        return str(nombre)
    else:
        return chr(nombre - 10 + ord('a'))

def decimal_vers_base(n, k):
    reste = n
    resultat = ""
    if n == 0:
        return '0'
    while reste > 0:
        a = reste % k
        b = nombre_vers_lettre(a)
        resultat = b + resultat
        reste //= k
    return resultat

def decimal_vers_hexadecimal(n):
    return decimal_vers_base(n, 16)