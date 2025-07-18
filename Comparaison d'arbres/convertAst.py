import ast

LEAFS = {ast.boolop, ast.Del, ast.operator, ast.unaryop, ast.cmpop, ast.Constant}

def addArrayOf(array: list) -> list:
    nodes = []
    for elem in array:
        nodes.extend(define_nodes(elem))
    return nodes

def addleafs(node: ast.AST) -> list:
    nodes = []
    for elem in LEAFS:
        if isinstance(node, elem):
            nodes.append(node)
            return nodes
    return nodes

def addBoolOp(node: ast.BoolOp) -> list:
    nodes = [node]
    nodes.append(node.op)
    nodes.extend(addArrayOf(node.values))
    return nodes

def addExpr(node: ast.Expr) -> list:
    lst = [node]
    lst.extend(define_nodes(node.value))
    return lst

def addAssign(node: ast.Assign) -> list:
    nodes = [node]
    nodes.extend(addArrayOf(node.targets))
    nodes.extend(define_nodes(node.value))
    return nodes

def addName(node: ast.Name) -> list:
    nodes = [node]
    if isinstance(node.ctx, ast.Del):
        nodes.append(node.ctx)
    return nodes

def addCompare(node: ast.Compare) -> list:
    nodes = [node]
    nodes.extend(define_nodes(node.left))
    nodes.extend(addArrayOf(node.ops))
    nodes.extend(addArrayOf(node.comparators))
    return nodes

def addIf(node: ast.If) -> list:
    nodes = [node]
    nodes.extend(define_nodes(node.test))
    nodes.extend(addArrayOf(node.body))
    nodes.extend(addArrayOf(node.orelse))
    return nodes

def addWhile(node: ast.While) -> list:
    nodes = [node]
    nodes.extend(define_nodes(node.test))
    nodes.extend(addArrayOf(node.body))
    nodes.extend(addArrayOf(node.orelse))
    return nodes

def addFor(node: ast.For) -> list:
    nodes = [node]
    nodes.extend(addArrayOf(node.orelse))
    nodes.extend(addArrayOf(node.body))
    return nodes

def addCall(node: ast.Call) -> list:
    nodes = [node]
    nodes.extend(addArrayOf(node.args))
    #Keywords skip
    return nodes

def addFunctionDef(node: ast.FunctionDef) -> list:
    nodes = [node]
    nodes.extend(addArrayOf(node.body))
    return nodes
def addImport(node: ast.Import):
    return [node]

def addImportFrom(node: ast.ImportFrom):
    return [node]

def addReturn(node: ast.Return):
    nodes = [node]
    nodes.extend(define_nodes(node.value))
    return nodes

def addBinOp(node: ast.BinOp):
    print("BinOppppppppppppppppppppppppppppppppppppppppppppp")
    nodes = [node]
    return nodes

def define_nodes(node):
    leaf = addleafs(node)
    if leaf != []:
        return leaf
    if isinstance(node, ast.Expr):
        return addExpr(node)
    if isinstance(node, ast.BoolOp):
        return addBoolOp(node)
    if isinstance(node, ast.Assign):
        return addAssign(node)
    if isinstance(node, ast.Name):
        return addName(node)
    if isinstance(node, ast.Compare):
        return addCompare(node)
    if isinstance(node, ast.While):
        return addWhile(node)
    if isinstance(node, ast.For):
        return addFor(node)
    if isinstance(node, ast.If):
        return addIf(node)
    if isinstance(node, ast.Call):
        return addCall(node)
    if isinstance(node, ast.FunctionDef):
        return addFunctionDef(node)
    if isinstance(node, ast.Import):
        return addImport(node)
    if isinstance(node, ast.ImportFrom):
        return addImportFrom(node)
    if isinstance(node, ast.Return):
        return addReturn(node)
    if isinstance(node, ast.BinOp):
        return addBinOp(node)
    elif hasattr(node, "body"):
        return addArrayOf(node.body)
    else:
         return []
