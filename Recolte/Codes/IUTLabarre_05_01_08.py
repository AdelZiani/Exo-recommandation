lst = [14, 7, 6, 12, 2, 3, 3, 10]

for x in lst:
    print(x - 2 * (x % 2) + 1, end=' ')