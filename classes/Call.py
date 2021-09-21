from classes.Symbol import Symbol
from classes.Tipo import TYPE
from classes.SymbolTable import SymbolTable
from classes.Asignacion import Asignacion
from classes.Value import Value
class Call:
    def __init__(self, id, args, row, col):
        self.id = id
        self.args = args
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        nscope = 'GLOBAL__FUNCTION__' + self.id
        t = tabla
        while t.padre != None:
            t = t.padre
        ntabla = SymbolTable(t)
        v = t.getSymbol(self.id)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        if(v.type == TYPE.FUNCTION):
            if(len(self.args)!=len(v.params)):
                return TYPE.ERROR
            for a in range(len(self.args)):
                val = self.args[a].execute(main, tabla, nscope)
                if(val == TYPE.ERROR):
                    return TYPE.ERROR
                if(v.params[a].type != TYPE.ANY and val.type != v.params[a].type):
                    return TYPE.ERROR
                res = ntabla.newSymbol(Symbol(v.params[a].id, val, nscope, self.row, self.col), TYPE.LOCAL)
                if(res == TYPE.ERROR):
                    return TYPE.ERROR
            for i in v.instructions:
                res = i.execute(main, ntabla, nscope)
                if(res == TYPE.ERROR):
                    return TYPE.ERROR
                if(res.type == TYPE.RETURN):
                    return res.val
            return Value(None, TYPE.NOTHING, self.row, self.col)
        return TYPE.ERROR