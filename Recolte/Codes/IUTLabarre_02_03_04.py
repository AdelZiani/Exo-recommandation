n = int(input('un entier positif: '))
message23ou4 = "divisible par 2, 3 ou 4"

if n % 2 == 0:
    print("divisible par 2")
if n % 3 == 0:
    print("divisible par 3")
if n % 4 == 0:
    print("divisible par 4")
if n % 2 != 0 and n % 3 != 0 and n % 4 != 0:
    print("pas divisible par 2, 3 ou 4")
