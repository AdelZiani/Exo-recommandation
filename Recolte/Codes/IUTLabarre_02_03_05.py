n = int(input('un entier positif: '))
message23ou4 = "divisible par 2, 3 ou 4"

flag = False
if n % 2 == 0:
    print("divisible par 2")
    flag = True
if n % 3 == 0:
    print("divisible par 3")
    flag = True
if n % 4 == 0:
    print("divisible par 4")
    flag = True
if not flag:
    print("pas divisible par 2, 3 ou 4")