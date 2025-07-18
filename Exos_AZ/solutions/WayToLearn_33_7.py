import re
adresse = "Rue 30, Quartier d'Aix-les-Bains"
print(re.sub('Quartier', 'Quart.', adresse))