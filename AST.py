class Node:

    count = 0
    type = 'Node (unspecified)'
    shape = 'ellipse'
   
    def __init__(self,children=None):
        self.ID = str(Node.count)
        Node.count+=1

        if not children: 
            self.children = []
        elif hasattr(children,'__len__'):
            self.children = children
        else:
            self.children = [children]
        self.next = []


    def addNext(self,next):
        self.next.append(next)


    def nodeTree(self, prefix=''):
        result = "%s%s\n" % (prefix, repr(self))

        for c in self.children:
            if not isinstance(c,Node):
                result += "%s Error: Child of type %r: %r\n" % (prefix,type(c),c)
                # result += c + '\n'
                continue
            result += c.nodeTree(prefix)
        return result

    def __str__(self):
        return self.nodeTree()
   
   
    def __repr__(self):
        return self.type


class TokenNode(Node):
    type = 'token'

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok
        
    def __repr__(self):
        return repr(self.tok)


class OpNode(Node):
    type = 'op'

    def __init__(self, op, children):
        Node.__init__(self,children)
        self.op = op
        try:
            self.nbargs = len(children)
        except AttributeError:
            self.nbargs = 1
         
    def __repr__(self):
        return "%s (%s)" % (self.op, self.nbargs)
   

class EntryNode(Node):
    type = 'ENTRY'

    def __init__(self):
        Node.__init__(self, None)


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


""" ARBOL AST: CLASES """

class Statement(Node):
    type = 'statement'

class Funcion(Node):
    type = 'function'
    
class FuncionNType(Node):
    type = 'funcion'

class Argumentos(Node):
    type = 'argv'

class Return(Node):
    type = 'return'

class VarNode(Node):
    type = 'var'

class WriteNode(Node):
    type = 'write'

class PromptNode(Node):
    type = 'prompt'

class IfNode(Node):
    type = 'if'

class ForNode(Node):
    type = 'for'

class AssignNode(Node):
    type = 'assign'

class CallFunNode(Node):
    type = 'callfun'
     
class IdNode(Node):
    type = 'ids'

class ExpresionesNode(Node):
    type = 'Expresiones'

class CondicionesNode(Node):
    type = 'Condiciones'

class LambdaNode(Node):
    type = 'lambda'
  
class WhileNode(Node):
    type = 'while'

class ElseNode(Node):
    type = 'else'