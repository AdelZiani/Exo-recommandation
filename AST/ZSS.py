import zss
import ast
import csv
import sys
import os

code = """
def range_append(n):
    lst=[]
    i = 1
    while i < n + 1:
        lst.append(i)
        i += 1
    return lst
"""

"""
def range_insert(n):
    lst=[]
    for i in range(n,0,-1):
        # insertion en fin de liste 
        lst.insert(0, i)
    return lst
"""

code2 ="""
def range_append(n):
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    return lst
"""

args = sys.argv

# Analyse du code en AST
tree1 = ast.parse(code)
tree2 = ast.parse(code2)

print(ast.dump(tree1, indent=4))
print("\n\n\n\n")

print(ast.dump(tree2, indent=4))

def convert_ast(tree):
    node = zss.Node(type(tree))
    for key in tree.__dict__:
        child = tree.__dict__[key]
        if type(child) == list:
            for elem in child:
                node.addkid(convert_ast(elem))
        elif isinstance(child, ast.AST):
            node.addkid(convert_ast(child))
    return node


def get_set(node):
    ret = set()
    ret.add(node.get_label(node))
    for elem in node.get_children(node):
        ret = ret | get_set(elem)
    return ret


def get_distances():
    def x(a):
        if a.get_label(a) in set1 and a.get_label(a) in set2:
            return 0
        return 1

    def y(a, b):
        i = 0
        if b.get_label(b) not in set1:
            i += 1
        if a.get_label(a) not in set2:
            i += 1
        return i

    solutions = os.listdir(args[1] +"/solutions")
    enonces = os.listdir(args[1] +"/enonces")
    with open('neighbour.csv',  mode='w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(["Enonce1", "Solution1", "Enonce2", "Solution2", "Score"])
        for elem in solutions:
            try:
                soluce = open(args[1] + "/solutions/" + elem, "r")
                enon = open(args[1] + "/enonces/" + elem.replace(".py", ".txt").replace("soluce", "énoncé"), "r")
                solution = soluce.read()
                soluce = convert_ast(ast.parse(solution))
                set1 = get_set(soluce)
            except SyntaxError:
                continue
            for elem2 in solutions:
                try:
                    soluce2 = open(args[1] + "/solutions/" + elem2, "r")
                    enon2 = open(args[1] + "/enonces/" + elem2.replace(".py", ".txt").replace("soluce", "énoncé"), "r")
                    solution2 = soluce2.read()
                    soluce2 = convert_ast(ast.parse(solution2))
                    set2 = get_set(soluce2)
                    dist = zss.distance(soluce, soluce2, zss.Node.get_children, x, x, y)
                    spamwriter.writerow([enon.read(), solution, enon2.read(), solution2, dist])
                except SyntaxError:
                    pass


                

get_distances()

"""
for i in range(1,100):
    dico = {}
    temoin = open("solutions/Github" + str(i) + ".py")
    temoin = temoin.read().removeprefix("```python").removesuffix("```")
    while temoin.endswith("\n") or temoin.startswith("\n"):
        temoin= temoin.removesuffix("\n").removeprefix("\n")
    temoin = temoin.removeprefix("```python").removesuffix("```")
    print("le code temoin : \n", temoin, "\n\n son ast: \n\n")
    print(ast.dump(ast.parse(temoin), indent=4)) 
    # Recherche de l'ast le plus proche
    for j in range(1, 100):
        f = open("solutions/Github" + str(j) + ".py")
        code = f.read()
        while code.endswith("\n") or code.startswith("\n"):
            code = code.removesuffix("\n").removeprefix("\n")
        code = code.removeprefix("```python").removesuffix("```")
        tree = ast.parse(code)
        dico[code] = zsrange_append',
            args=argumentss.simple_distance(convert_ast(ast.parse(temoin)), convert_ast(tree))
    plus_petits = sorted(dico.items(), key=lambda x: x[1])[:3]
    cles_plus_petites = [cle for cle, val in plus_petits]
    for elem in cles_plus_petites:
        print("voisin : \n", elem)
    print("------------------------------------------------------------------------------------------------------------------------")"""

"""
This function return 5 
"""