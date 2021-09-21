from classes.ArrayAccess import ArrayAccess
from classes.Value import Value
from classes.Symbol import Symbol
from classes.Tipo import TYPE
class Declaracion:
    def __init__(self, id, val, row, col):
        self.id = id
        self.val = val
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        val = self.val
        if(self.val != None):
            val = self.val.execute(main, tabla, scope)
        if(val==TYPE.ERROR):
            return TYPE.ERROR
        res = tabla.newSymbol(Symbol(self.id, val, scope, self.row, self.col), TYPE.GLOBAL)
        if(res == TYPE.ERROR):
            return TYPE.ERROR
        return Value(None, TYPE.NOTHING, self.row, self.col)