from classes.Tipo import TYPE


class Global:
    def __init__(self):
        self.instrucciones = []
        self.symbols = []
        self.errors = []
        self.ast = []
        self.output = ""
        self.ts = []

    def newPrint(self, mensaje):
        self.output += mensaje
    
    def execute(self):
        for i in range(len(self.instrucciones)):
            instruccion = self.instrucciones[i]
            res = instruccion.execute(self, self.ts)
            if(res == TYPE.ERROR):
                break
        if(self.output[-1]=='\n'):
            self.output = self.output[0:-1]

        