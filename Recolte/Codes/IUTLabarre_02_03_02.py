n = int(input('un entier positif: '))
message23ou4 = "divisible par 2, 3 ou 4"
if n % 2 == 0:
    print(message23ou4)
elif n % 3 == 0:
    print(message23ou4)
elif n % 4 == 0:
    print(message23ou4)
else:
    print("pas " + message23ou4)