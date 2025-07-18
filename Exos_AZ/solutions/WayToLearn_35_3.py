class Etudiant:
    nom_etudiant = 'Alex Babtise'
    notes = 96  

# Afficher les valeurs originales
print(f"Nom de l'étudiant: {getattr(Etudiant, 'nom_etudiant')}")
print(f"Notes: {getattr(Etudiant, 'notes')}")

# Modifier les valeurs des attributs
setattr(Etudiant, 'nom_etudiant', 'Emily Finoris')
setattr(Etudiant, 'notes', 88) 

# Afficher les valeurs modifiées 
print(f"Nom de l'étudiant: {getattr(Etudiant, 'nom_etudiant')}")
print(f"Notes: {getattr(Etudiant, 'notes')}")