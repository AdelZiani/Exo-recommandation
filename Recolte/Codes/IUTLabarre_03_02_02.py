n = int(input("Entrez un entier n positif: "))

for m in range(n+1):
    isprime = True
    for i in range(2, m):
        if m % i == 0:
            isprime = False
    if m >= 2 and isprime:
        print(m, "est premier")