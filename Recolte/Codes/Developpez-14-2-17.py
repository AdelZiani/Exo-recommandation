# -*- coding : utf8 -*-
"""Liste d'entiers différents."""



t = [2, 20, 10, 25 ,26 ,23, 24, 25, 5, 4, 54, 6, 32, 2]

# Sont-ils différents ?
tousDiff = True
i = 0
while tousDiff and i < (n-1) :
    j = i + 1
    while tousDiff and j < n :
        if t[i] == t[j]:
            tousDiff = False
        else :
            j += 1
    i += 1

if tousDiff :
    print("\nTous les éléments sont distincts.")
else :
    print("\nAu moins une valeur est répétée.")
print(t)

