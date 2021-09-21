from classes.Declaracion import Declaracion
from classes.SymbolTable import SymbolTable
from classes.Tipo import TYPE


class Global:
    def __init__(self):
        self.instrucciones = []
        self.symbols = SymbolTable()
        self.errors = []
        self.ast = None
        self.output = ""

    def newPrint(self, mensaje):
        self.output += mensaje
    
    def execute(self):
        scope = 'GLOBAL'
        for j in self.instrucciones:
            if(isinstance(j, Declaracion)):
                j.execute(self, self.symbols, scope)
        for i in self.instrucciones:
            if(isinstance(i, Declaracion)):
                continue
            i.execute(self, self.symbols, scope)
        if((len(self.output)>0) and (self.output[-1]=='\n')):
            self.output = self.output[0:-1]

        