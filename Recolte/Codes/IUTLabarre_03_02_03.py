n = int(input("Entrez un entier n positif: "))

count = 0
for m in range(n+1):
    isprime = True
    for i in range(2, m):
        if m % i == 0:
            isprime = False
    if m >= 2 and isprime:
        count += 1
        
print("il y a", count, "nombres premiers entre 1 et", n)