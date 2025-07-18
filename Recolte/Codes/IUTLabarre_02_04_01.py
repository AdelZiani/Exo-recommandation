print('Premier nombre')
a = int(input())
print('Second nombre')
b = int(input())
print('Troisieme nombre')
c = int(input())

if a < b: # pour le min, inverser les signes
    if b < c:
        print(c)
    else:
        print(b)
else:
    if a < c:
        print(c)
    else:
        print(a)