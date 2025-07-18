b = float(input("Entrer la base: "))
e = int(input("Entrer l'exposant: "))
puissance = 1
  
for i in range(e): 
	puissance = puissance * b
 
print("{0} ^ {1} = {2}".format(b,e,puissance))