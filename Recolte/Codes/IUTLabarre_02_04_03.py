print('Premier nombre')
a = int(input())
print('Second nombre')
b = int(input())
print('Troisieme nombre')
c = int(input())

if b > a:
    maxab = b
else:
    maxab = a
if c > maxab:
    print(c)
else:
    print(maxab)