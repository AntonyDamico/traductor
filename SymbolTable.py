class SymbolTable:

    def __init__(self):
        self.variables = {}

    def createVariable(self, name, value=None):
        self.variables[name] = value

    def updateVariable(self, name, newValue):
        if(name in self.variables):
            self.variables[name] = newValue
            return
        raise Exception('The variable ' + str(name) + ' must be initialized')

    def readVariable(self, name):
        if(name in self.variables):
            return self.variables[name]
        raise Exception('The variable ' + name + ' must be initialized')

    def __str__(self):
        if (self.variables == {}): return 'empty'
        final = ''
        final += '-----------------------\n'
        for variable in self.variables:
            final += variable + ' => ' + str(self.variables[variable])
        final += '\n-----------------------'
        return final
