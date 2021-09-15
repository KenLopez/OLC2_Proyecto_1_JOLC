from classes.Symbol import Symbol
from classes.Tipo import TYPE
class Asignacion:
    def __init__(self, id, val, type, row, col):
        self.symbol  = Symbol(id, val, '', row, col)
        self.type = type
    
    def execute(self, main, table, scope):
        self.symbol.val = self.symbol.val.execute(main, table, scope)
        if(self.symbol.val==TYPE.ERROR):
            return TYPE.ERROR
        self.symbol.scope = scope
        if(self.type == TYPE.ANY):
            table.updateSymbol(self.symbol)
            return TYPE.NOTHING
        elif(self.type == self.symbol.val.type):
            table.updateSymbol(self.symbol)
            return TYPE.NOTHING
        else:
            return TYPE.ERROR
