import ast
from functools import singledispatch

import statistics

arithmeticOperators = [ast.Add, ast.Sub, ast.MatMult, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.FloorDiv]

bytesOperators = [ast.RShift, ast.LShift, ast.BitXor, ast.BitAnd, ast.BitOr]

cmp = [ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE]

testin = [ast.In, ast.NotIn]

testis = [ast.Is, ast.IsNot]

@singledispatch
def compare(node1, node2):
    return -1


@compare.register
def _(node1: ast.boolop, node2: ast.AST):
    print("Traitement spécifique pour ast.Del")
    if node2 == node1:
        print("égalité parafaite")
        return 100
    elif isinstance(node2, ast.boolop):
        return 90
    elif isinstance(node2, ast.Not):
        return 85
    return 0

@compare.register
def _(node1: ast.operator, node2: ast.AST):
    print("Traitement spécifique pour ast.operator")
    if node2 == node1:
        print("égalité parafaite")
        return 100
    if (node1 in arithmeticOperators and node2 in arithmeticOperators) or (node1 in bytesOperators and node2 in bytesOperators):
        return 90
    if isinstance(node2, ast.operator):
        return 20
    if node1 in bytesOperators and node2 == ast.Invert:
        return 85
    if node1 in arithmeticOperators and (node2 == ast.UAdd or node2 == ast.USub):
        return 85
    return 0

@compare.register
def _(node1: ast.unaryop, node2: ast.AST):
    print("Traitement spécifique pour ast.operator")
    if node2 == node1:
        print("égalité parafaite")
        return 100
    if ( (isinstance(node1, ast.UAdd) or isinstance(node1, ast.USub)) and node2 in arithmeticOperators) or (isinstance(node1, ast.Invert) and node2 in bytesOperators) or (node1.isinstance(ast.Not) and node2.isinstance(ast.boolop)):
        return 90

    if(isinstance(node1, ast.UAdd) and isinstance(node2, ast.USub) or isinstance(node2, ast.UAdd) and isinstance(node1, ast.USub)):
        return 95
    if isinstance(node2, ast.unaryop):
        return 20
    return 0
    
@compare.register
def _(node1: ast.cmpop, node2: ast.AST):
    print("Traitement spécifique pour ast.operator")
    if node2 == node1:
        print("égalité parafaite")
        return 100
    if ( (node1 in cmp and node2 in cmp) or (node1 in testin and node2 in testin) or (node1 in testis and node2 in testis)) :
        return 95
    if(isinstance(node2, ast.cmpop)):
        return 20
    return 0
    
@compare.register
def _(node1: ast.Constant, node2: ast.AST):
    if not isinstance(node2, ast.Constant):
        return 0
    if type(node1.value) == type(node2.value):
        return 100
    return 85
    
@compare.register
def _(node1: ast.Name, node2: ast.AST):
    if not isinstance(node2, ast.Name):
        return 0
    if node1.ctx == node2.ctx:
        return 100
    return 80

@compare.register
def _(node1: ast.Call, node2: ast.AST):
    if not isinstance(node2, ast.Call):
        return 0
    if (len(node1.args) == 0 and len(node2.args) == 0) or (len(node1.args) > 1 and len(node2.args) > 1) or (len(node1.args) == 1 and len(node2.args) == 1) :
        return 100
    if (len(node1.args) == 1 and len(node2.args) > 1) or (len(node1.args) > 1 and len(node2.args) == 1):
        return 90
    return 80

#@compare.register
#def _(node1: ast.Compare, node2: ast.AST):
#    if not isinstance(node2, ast.Compare):
#        return 0
#    if (len(node1.args) == 0 and len(node2.args) == 0) or (len(node1.args) > 1 and len(node2.args) > 1) or (len(node1.args) == 1 and len(node2.args) == 1) :
#        return 100
#    if (len(node1.args) == 1 and len(node2.args) > 1) or (len(node1.args) > 1 and len(node2.args) == 1):
#        return 90
#    return 80



@compare.register
def _(node1: ast.If, node2: ast.AST):
    print("Traitement spécifique pour ast.If")
    if isinstance(node2, ast.If):
        return 100
    return 0


@compare.register
def _(node1: ast.While, node2: ast.AST):
    print("Traitement spécifique pour ast.If")
    if isinstance(node2, ast.While):
        return 100
    if isinstance(node2, ast.For):
        return 80
    return 0

@compare.register
def _(node1: ast.For, node2: ast.AST):
    print("Traitement spécifique pour ast.For")
    if isinstance(node2, ast.For):
        return 100
    if isinstance(node2, ast.While):
        return 80
    return 0


@compare.register
def _(node1: ast.FunctionDef, node2: ast.AST):
    if not isinstance(node2, ast.FunctionDef):
        return 0
    if (len(node1.args) == 0 and len(node2.args) == 0) or (len(node1.args) > 1 and len(node2.args) > 1) or (len(node1.args) == 1 and len(node2.args) == 1) :
        return 100
    if (len(node1.args) == 1 and len(node2.args) > 1) or (len(node1.args) > 1 and len(node2.args) == 1):
        return 90
    return 80

@compare.register
def _(node1: ast.Assign, node2: ast.AST):
    if not isinstance(node2, ast.Assign):
        return 0
    return 100


@compare.register
def _(node1: ast.Import, node2: ast.AST):
    tot = 0
    if isinstance(node2, ast.Import):
        tot += 90
    elif isinstance(node2, ast.ImportFrom):
        tot += 75
    else:
        return 0
    if len(node2) > 1 and len(node1) > 1 :
        return tot + 10
    if len(node2) == 1 and len(node1) == 1:
        return tot + 10
    return tot

@compare.register
def _(node1: ast.ImportFrom, node2: ast.AST):
    tot = 0
    if isinstance(node2, ast.ImportFrom):
        tot += 90
    elif isinstance(node2, ast.Import):
        tot += 75
    else:
        return 0
    if len(node2) > 1 and len(node1) > 1 :
        return tot + 10
    if len(node2) == 1 and len(node1) == 1:
        return tot + 10
    return tot

@compare.register
def _(node1: ast.Return, node2: ast.AST):
    if not isinstance(node2, ast.Return):
        return 0
    if node1.value == None and node2.value == None:
        return 100
    if node1.value != None and node2.value != None:
        return 100
    return 90

@compare.register
def _(node1: ast.BinOp, node2: ast.AST):
    if not isinstance(node2, ast.BinOp):
        return 0
    if node2.op == node1.op:
        return 100
    return 90

@compare.register
def _(node1: ast.UnaryOp, node2: ast.AST):
    if node2 == node1:
        return 100
    if isinstance(node2, ast.UnaryOp):
        return 90
    return 0


def cleanNodes(lst):
    ret = []
    for i in range(len(lst)):
        good = True
        for j in range(i + 1, len(lst)):
            if compare(lst[i], lst[j]) == 100:
                good = False
        if good:
            ret.append(lst[i])
    return ret



def compareNodes(nodes1: list, nodes2: list) -> int:
    dist1 = []
    dist2 = []
    nodes1 = cleanNodes(nodes1)
    nodes2 = cleanNodes(nodes2)
    for elem in nodes1:
        max = -1
        for elem2 in nodes2:
            dist = compare(elem, elem2)
            if dist > max:
                max = dist
        if max >= 0:
            dist1.append(max)
    for elem in nodes2:
        max = -1
        for elem2 in nodes1:
            dist = compare(elem, elem2)
            if dist > max:
                max = dist
        if max >= 0:
            if max == 0:
                print(elem, " rien pour lui")
            dist2.append(max)
    print (statistics.mean(dist1), statistics.mean(dist2))
    print(dist1, dist2)