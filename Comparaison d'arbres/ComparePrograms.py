from convertAst import define_nodes
from CompareNodes import compareNodes
import ast

code1 = """
5*5
"""

code2 = """
5+5
"""


tree1 = ast.parse(code1)

print(ast.dump(tree1, indent=4))  # Python 3.9+
lst1 = define_nodes(tree1)

tree2 = ast.parse(code2)
print(ast.dump(tree2, indent=4))  # Python 3.9+
lst2 = define_nodes(tree2)

print(lst1, "\n\n", lst2)

compareNodes(lst1, lst2)