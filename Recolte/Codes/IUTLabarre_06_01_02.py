from random import randint

t1 = [[8, 3, 3, 3], [5, 6, 1, 5], [0, 7, 9, 1]]

for i in range(len[t1]):
    for j in range(len(t1[i])):
        print (t1[i][j], end=' ')
    print()

n = randint(1, 9)

t1[-1][0] = n

for i in range(len[t1]):
    for j in range(len(t1[i])):
        print (t1[i][j], end=' ')
    print()