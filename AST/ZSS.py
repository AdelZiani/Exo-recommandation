#bibliothèque contenant l'algo de Zhang-Shasha
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

# Création des AST
tree1 = ast.parse(code)
tree2 = ast.parse(code2)

print(ast.dump(tree1, indent=4))
print("\n\n\n\n")

print(ast.dump(tree2, indent=4))


#Cette fonction convertit les AST données par la lib ast en AST pour Zhang-Shasha
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



#créé un set contenant tout les noeuds de l'abre enraciné en node
def get_set(node):
    ret = set()
    ret.add(node.get_label(node))
    for elem in node.get_children(node):
        ret = ret | get_set(elem)
    return ret


#Crée un fichier CSV avec toutes les pairs d'exercices contenus dans le repo args[1] et leurs distances Zhang-Shasha.
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