print('Premier nombre')
a = int(input())
print('Second nombre')
b = int(input())
print('Troisieme nombre')
c = int(input())

if a < b:
    if b < c:
        print(b)
    elif a < c:
        print(c)
    else:
        print(a)
else:
    if a < c:
        print(a)
    elif b < c:
        print(c)
    else:
        print(b)