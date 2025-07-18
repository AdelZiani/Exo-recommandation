try:
	l = [1, 2, 3, 4, 5]
	# Essayer d'accéder à l'attribut 'length' de la liste 'l' et de l'affecter à 'r'.
	r = l.length  # Essayer d'accéder à l'attribut length
	print("Longueur de la liste:", r)
except AttributeError:
	print("Erreur: La liste n'a pas d'attribut length.")