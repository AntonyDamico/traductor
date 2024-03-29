from SymbolTable import SymbolTable

table = SymbolTable()


class Node:

    count = 0
    type = 'Node (no type)'

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1

        if not children:
            self.children = []
        elif hasattr(children, '__len__'):
            self.children = children
        else:
            self.children = [children]
        self.next = []

    def eval_all(self):
        # print(self.__class__.__name__)
        # print(self.children)
        print('====================')
        if(len(self.children) < 2):
            self.eval()
        for c in self.children:
            if(c.children):
                c.eval()

    def eval(self):
        print('pass')
        pass

    def addNext(self, next):
        self.next.append(next)

    def nodeTree(self):
        result = "%s%s\n" % (repr(self))

        for c in self.children:
            if not isinstance(c, Node):
                result += "Error: Child of type %r: %r\n" % (
                    type(c), c)
                # result += c + '\n'
                continue
            result += c.nodeTree()
        return result

    def __str__(self):
        return self.nodeTree()



class TokenNode(Node):
    type = 'token'

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok

    def eval(self):
        if(isinstance(self.tok, str)):
           if(self.tok[0] == "'" or self.tok[0] == '"'):
               return self.tok[1:-1] 
        return self.tok


class OpNode(Node):
    type = 'op'

    def __init__(self, op, children):
        Node.__init__(self, children)
        self.op = op
        try:
            self.nbargs = len(children)
        except AttributeError:
            self.nbargs = 1


    def eval(self):
        first = self.children[0].eval()
        second = self.children[1].eval()

        if(isinstance(first, str) or isinstance(second, str)):
            first = str(first)
            second = str(second)

        if(self.op == '+'):
            return first + second
        if(self.op == '-'):
            return first - second
        if(self.op == '*'):
            return first * second
        if(self.op == '/'):
            return first / second
        if(self.op == '%'):
            return first % second
        if(self.op == '<'):
            return first < second
        if(self.op == '>'):
            return first > second
        if(self.op == '<='):
            return first <= second
        if(self.op == '>='):
            return first >= second
        if(self.op == '=='):
            return first == second


class UnOpNode(Node):
    type = 'Unary'

    def __init__(self, op, children):
        Node.__init__(self, children)
        self.op = op

    def eval(self):
        global table
        if(self.op == '++'):
            table.updateVariable(
                self.children[0].name, self.children[0].eval() + 1)
        if(self.op == '--'):
            table.updateVariable(
                self.children[0].name, self.children[0].eval() - 1)



class Statement(Node):
    type = 'statement'

    def eval(self):
        for c in self.children:
            c.eval()


class VarNode(Node):
    type = 'var'

    def eval(self):
        global table
        # print(table)
        table.createVariable(self.children[0].eval(), self.children[1].eval())


class WriteNode(Node):
    type = 'write'

    def eval(self):
        print('> ' + str(self.children[0].eval()))


class IfNode(Node):
    type = 'if'

    def eval(self):
        # print(self.children)

        childrenCount = len(self.children)
        if(childrenCount == 2):
            if(self.children[0].eval()):
                self.children[1].eval()

        elif(childrenCount == 3):
            if(self.children[0].eval()):
                self.children[1].eval()
            else:
                self.children[2].eval()


class ForNode(Node):
    type = 'for'

    def eval(self):
        self.children[0].eval()
        while(self.children[1].eval()):
            self.children[2].eval()
            self.children[3].eval()


class AssignNode(Node):
    type = 'assign'

    def eval(self):
        global table
        table.updateVariable(self.children[0].eval(), self.children[1].eval())


class IdNode(Node):
    type = 'id'

    def __init__(self, children):
        Node.__init__(self, children)
        self.name = self.children[0].eval()

    def eval(self):
        global table
        return table.readVariable(self.children[0].eval())


class WhileNode(Node):
    type = 'while'

    def eval(self):
        while(self.children[0].eval()):
            self.children[1].eval()


class ElseNode(Node):
    type = 'else'
