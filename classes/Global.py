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
        for i in range(len(self.instrucciones)):
            instruccion = self.instrucciones[i]
            instruccion.execute(self, self.symbols, 'GLOBAL')
        if((len(self.output)>0) and (self.output[-1]=='\n')):
            self.output = self.output[0:-1]

        