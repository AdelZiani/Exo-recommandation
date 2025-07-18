# Définir une classe appelée FileDAttente pour implémenter une structure de données de file d'attente.
class FileDAttente:
    # Initialiser la file d'attente avec une liste vide pour stocker les éléments
    def __init__(self):
        self.items = []

    # Ajouter un élément à la fin de la file d'attente
    def insert(self, item):
        self.items.append(item)

    # Retirer et renvoyer un élément du début de la file d'attente si celle-ci n'est pas vide
    def remove(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Impossible de retirer d'une file d'attente vide.")

    # Vérifier si la file d'attente est vide
    def is_empty(self):
        return len(self.items) == 0


# Créer une instance de la classe FileDAttente
f = FileDAttente()

# Ajouter des éléments à la file d'attente
f.insert(6)
f.insert(1)
f.insert(3)
f.insert(5)
f.insert(8)

# Afficher les éléments actuels de la file d'attente
print("File d'attente actuelle:", f.items)

# Retirer les éléments du début de la file d'attente et afficher les éléments retirés de la file d'attente.
removed_item = f.remove()
print("Élément retiré de la file d'attente:", removed_item)
removed_item = f.remove()
print("Élément retiré de la file d'attente:", removed_item)

# Afficher les éléments mis à jour dans la file d'attente
print("File d'attente mise à jour:", f.items) 