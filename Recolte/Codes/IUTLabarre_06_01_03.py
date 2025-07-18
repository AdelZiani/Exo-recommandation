from random import randrange
t2 = list()
for i in range(5):
    ligne = list()
    for j in range(7):
        ligne.append(randrange(10))
    t2.append(ligne)
print(t2)