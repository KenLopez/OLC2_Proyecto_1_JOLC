from classes.Value import Value
from classes.Tipo import TYPE

class Logica:
    def __init__(self, expIzq, expDer, type, row, col):
        self.expIzq = expIzq
        self.expDer = expDer
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla):
        der = self.expDer.execute(main, tabla)
        izq = self.expIzq.execute(main, tabla)
        if((izq.type == TYPE.TYPEBOOL) and (der.type == TYPE.TYPEBOOL)):
            if(self.type == TYPE.LOGICAND):
                return Value((izq.val and der.val), TYPE.TYPEBOOL, self.row, self.col)
            elif(self.type == TYPE.LOGICOR):
                return Value((izq.val or der.val), TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        elif(izq.type == TYPE.TYPEBOOL):
            if(self.type == TYPE.NOT):
                return Value((not izq.val), TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        else:
            return TYPE.ERROR
