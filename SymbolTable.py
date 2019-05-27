class SymbolTable:

    def __init__(self):
        self.variables = {}

    def createVariable(self, name, value = None):
        self.variables[name] = value

    def readVariable(self, name):
        if(name in self.variables): 
            return self.variables[name]
        raise Exception('The variable ' + name + ' must be initialized')