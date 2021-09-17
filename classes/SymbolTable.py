from classes.Value import Value
from classes.Tipo import TYPE

class SymbolTable:
    def __init__(self, padre = None):
        self.padre = padre
        self.symbols = {}

    def newSymbol(self, symbol, type):
        s = self.getSymbol(symbol.id, type)
        if(s == TYPE.ERROR):
            self.symbols[symbol.id] = symbol
        else:
            return TYPE.ERROR
        return Value(None, TYPE.NOTHING, symbol.row, symbol.col)
    
    def updateSymbol(self, symbol, type=TYPE.NOTHING):
        s = self.getSymbol(symbol.id, type)
        if(s != TYPE.ERROR):
            s.type = symbol.val.type
            s.val = symbol.val.val
        else:
            self.symbols[symbol.id] = symbol
        return Value(None, TYPE.NOTHING, symbol.row, symbol.col)

    def getSymbol(self, id, type = TYPE.NOTHING):
        s = self.symbols.get(id)
        if(s!=None):
            if((type != TYPE.GLOBAL) or (self.padre == None)):
                return s.val
        if(self.padre == None):
            return TYPE.ERROR
        if(type != TYPE.LOCAL):
            res = self.padre.getSymbol(id, type)
            if(res==TYPE.ERROR):
                return TYPE.ERROR
            return res
        return TYPE.ERROR