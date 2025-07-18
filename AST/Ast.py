import ast

code = """
if a >2:
    a = a>2
"""

code = """
[2,2,3]
a = 2
"""


# Analyse du code en AST
tree = ast.parse(code)
print(tree)
# Affichage de l’AST brut
print(ast.dump(tree, indent=4))  # Python 3.9+
