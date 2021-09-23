import base64
from classes.Declaracion import Declaracion
from classes.SymbolTable import SymbolTable
from classes.Tipo import TYPE
import graphviz

class Global:
    def __init__(self):
        self.instrucciones = []
        self.symbols = SymbolTable()
        self.errors = []
        self.ast = None
        self.output = ""
        self.graph = ""
        self.input = ""

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
        if len(self.errors) == 0:
            self.graphTree()
    
    def graphTree(self):
        dot = graphviz.Graph(comment='ast')
        dot.node('nodo'+str(id(self.ast)), self.ast.tag)
        self.ast.graficar(dot)
        self.graph = dot.source
    
    def getGraph(self):
        dot = graphviz.Source(self.graph)
        coded = base64.b64encode(dot.pipe(format='png')).decode('utf-8')
        return coded

        