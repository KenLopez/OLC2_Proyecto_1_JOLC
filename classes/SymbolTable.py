from classes.Value import Value
from classes.Tipo import TYPE

class SymbolTable:
    def __init__(self, padre = None):
        self.padre = padre
        self.symbols = {}
    
    def updateSymbol(self, symbol):
        s = self.symbols.get(symbol.id)
        if(s!=None):
            s.val = symbol.val
            return Value(None, TYPE.NOTHING, self.symbol.row, self.symbol.col)
        else:
            if(self.padre == None):
                self.symbols[symbol.id] = symbol
            else:
                res = self.padre.updateSymbol(symbol)
                if(res == TYPE.ERROR):
                    return TYPE.ERROR
                else:
                    return Value(None, TYPE.NOTHING, self.symbol.row, self.symbol.col)
        return TYPE.ERROR

    def getSymbol(self, id):
        s = self.symbols.get(id)
        if(s!=None):
            return s.val
        else:
            if(self.padre == None):
                return TYPE.ERROR
            else:
                res = self.padre.getSymbol(id)
                if(res==TYPE.ERROR):
                    return TYPE.ERROR
                else:
                    return res