from classes.Value import Value
from classes.Symbol import Symbol
from classes.Variable import Variable
from classes.Asignacion import Asignacion
from classes.Tipo import TYPE
from classes.SymbolTable import SymbolTable
class For:
    def __init__(self, variable, range, instrucciones, row, col):
        self.variable = variable
        self.range = range
        self.instrucciones = instrucciones
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        nscope = scope + '_FOR'
        v = self.range.execute(main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        ntabla = SymbolTable(tabla)
        if(v.type == TYPE.TYPELIST):
            for i in v.val:
                ntabla.updateSymbol(Symbol(self.variable, i, nscope, self.row, self.col), TYPE.LOCAL)
                ftabla = SymbolTable(ntabla)
                for j in self.instrucciones:
                    res = j.execute(main, ftabla, nscope)
                    if(res == TYPE.ERROR):
                        return TYPE.ERROR
            return Value(None, TYPE.NOTHING, self.row, self.col)
        if(v.type == TYPE.TYPESTRING):
            for i in v.val:
                ntabla.updateSymbol(Symbol(self.variable, Value(i, TYPE.TYPESTRING, self.row, self.col), nscope, self.row, self.col), TYPE.LOCAL)
                ftabla = SymbolTable(ntabla)
                for j in self.instrucciones:
                    res = j.execute(main, ftabla, nscope)
                    if(res == TYPE.ERROR):
                        return TYPE.ERROR
            return Value(None, TYPE.NOTHING, self.row, self.col)
        if(v.type == TYPE.RANGE):
            v1 = v.val[0].execute(main, tabla, nscope)
            v2 = v.val[1].execute(main, tabla, nscope)
            if((v1==TYPE.ERROR) or (v1.type != TYPE.TYPEINT64)):
                return TYPE.ERROR
            if((v2==TYPE.ERROR) or (v2.type != TYPE.TYPEINT64)):
                return TYPE.ERROR
            for i in range(v1.val,v2.val+1):
                ntabla.updateSymbol(Symbol(self.variable, Value(i, TYPE.TYPEINT64, self.row, self.col), nscope, self.row, self.col), TYPE.LOCAL)
                ftabla = SymbolTable(ntabla)
                for j in self.instrucciones:
                    res = j.execute(main, ftabla, nscope)
                    if(res == TYPE.ERROR):
                        return TYPE.ERROR
                    if(res.type == TYPE.CONTINUE):
                        break
                    if(res.type == TYPE.BREAK):
                        res = res.execute(main, tabla, scope)
                        if (res == TYPE.ERROR):
                            return Value(None, TYPE.NOTHING, self.row, self.col)
                        return res
                    if(res.type == TYPE.RETURN):
                        return res
                else:
                    continue
            return Value(None, TYPE.NOTHING, self.row, self.col)
        return TYPE.ERROR
