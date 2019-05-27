class SymbolTable:

    def __init__(self):
        self.variables = {}

    def createVariable(self, name, value = None):
        self.variables[name] = value

    def readVariable(self, name):
        return self.variables[name]