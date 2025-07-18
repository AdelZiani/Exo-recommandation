from random import randint

n=randint(10, 20)

lst_random10 = []
for _ in range(n):
    lst_random10.append(randint(0,10))
print(lst_random10)
print(len(lst_random10))