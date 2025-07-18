n = int(input('un entier positif: '))

if n % 3 == 0:
    if n % 4 == 0:
        print("divisible par 12")
    else:
        print("divisible par 3 mais pas par 12")
elif n % 4 == 0:
    print("divisible par 4 mais pas par 12")
else:
    print("pas divisible par 3 ou 4")