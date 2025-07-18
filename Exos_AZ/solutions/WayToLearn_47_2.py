# Importer la fonction 'reduce' du module 'functools'
from functools import reduce

# Définir une fonction lambda 'fibonacci' qui génère une série de Fibonacci jusqu'à 'n' éléments
# Elle utilise la fonction 'reduce()' avec une fonction lambda et une liste initiale [0, 1] pour générer la série de Fibonacci.
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print("Série de Fibonacci jusqu'à 2:")
print(fibonacci(2))

print("\nSérie de Fibonacci jusqu'à 10:")
print(fibonacci(10))