print('Premier nombre')
a = int(input())
print('Second nombre')
b = int(input())
print('Troisieme nombre')
c = int(input())


if a > b:
    tmp = a
    a = b
    b = tmp
if c < a:
    tmp = c
    c = b
    b = a
    a = tmp
elif c < b:
    tmp = c
    c = b
    b = tmp
print(a, b, c)