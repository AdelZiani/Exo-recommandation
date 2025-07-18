# Créer la classe 'Etudiant'
class Etudiant:

	# Constructeur
	def __init__(self, nom, matricule, notes1, notes2):
		self.nom = nom
		self.matricule = matricule
		self.notes1 = notes1
		self.notes2 = notes2

	# Fonction permettant de créer et d'ajouter un nouvel étudiant
	def accepter(self, nom, matricule, notes1, notes2):
		e = Etudiant(nom, matricule, notes1, notes2)
		liste.append(e)

	# Fonction permettant d'afficher les détails de l'étudiant
	def display(self, e):
		print("Nom : ", e.nom)
		print("Matricule : ", e.matricule)
		print("Notes1 : ", e.notes1)
		print("Notes2 : ", e.notes2)
		print("\n")

	# Fonction de recherche
	def rechercher(self, mat):
		for i in range(liste.__len__()):
			if(liste[i].matricule == mat):
				return i

	# Fonction de suppression
	def delete(self, mat):
		i = obj.rechercher(mat)
		del liste[i]

	# Fonction de mise à jour
	def update(self, mat, No):
		i = obj.rechercher(mat)
		mat1 = No
		liste[i].matricule = mat1


# Créer une liste pour ajouter des étudiants
liste = []
# un objet de la classe Etudiant
obj = Etudiant('', 0, 0, 0)

print("\nOpérations utilisées: ")
print("\n1.Accepter les détails de l'étudiant\n2.Afficher les détails de l'étudiant\n3.Rechercher les détails d'un étudiant\n4.Supprimer les détails de l'étudiant\n5.Mettre à jour les détails de l'étudiant\n6.Quitter")

# ch = int(input("Entrer un choix:"))
# if(ch == 1):
obj.accepter("Alex", 1, 98, 90)
obj.accepter("Bob", 2, 85, 45)
obj.accepter("Jean", 3, 70, 60)

# elif(ch == 2):
print("\n")
print("\nListe des étudiants\n")
for i in range(liste.__len__()):
	obj.display(liste[i])

# elif(ch == 3):
print("\nÉtudiant trouvé:")
s = obj.rechercher(2)
obj.display(liste[s])

# elif(ch == 4):
obj.delete(2)
print(liste.__len__())
print("Liste après suppression:")
for i in range(liste.__len__()):
	obj.display(liste[i])

# elif(ch == 5):
obj.update(3, 2)
print(liste.__len__())
print("Liste après mise à jour")
for i in range(liste.__len__()):
	obj.display(liste[i])

# else:
print("Good Bye!")