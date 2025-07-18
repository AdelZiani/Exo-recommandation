# Définir une fonction lambda 'commence_par' qui vérifie si une chaîne donnée commence par 'A'.
commence_par = lambda x: True if x.startswith('A') else False

# Vérifier si la chaîne commence par 'A' en utilisant la fonction lambda 'commence_par'.
# Afficher le résultat qui sera 'True' si la chaîne commence par 'A', sinon 'False'.
print(commence_par('Alex'))
print(commence_par('Bob')) 