n = int(input("Entrez un entier n positif: "))
isprime = True
for i in range(2, n):
    if n % i == 0:
        isprime = False
if n >= 2 and isprime:
    print(n, "est premier")
else:
    print(n, "n'est pas premier")