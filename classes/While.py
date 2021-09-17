from classes.SymbolTable import SymbolTable
from classes.Value import Value
from classes.Tipo import TYPE
class While:
    def __init__(self, condition, instructions, row, col):
        self.condition = condition
        self.instructions = instructions
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        nscope = scope + "_WHILE"
        v = self.condition.execute(main, tabla, nscope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        if(v.type != TYPE.TYPEBOOL):
            return TYPE.ERROR
        while v.val:
            ntabla = SymbolTable(tabla)
            for i in range(len(self.instructions)):
                res = self.instructions[i].execute(main, ntabla, nscope)
                if(res == TYPE.ERROR):
                    return TYPE.ERROR
                if(res.type == TYPE.CONTINUE):
                        break
                if(res.type == TYPE.BREAK):
                    res = res.execute(main, tabla, scope)
                    if (res == TYPE.ERROR):
                        return Value(None, TYPE.NOTHING, self.row, self.col)
                    return res
            else:
                v = self.condition.execute(main, ntabla, nscope)
                if(v == TYPE.ERROR):
                    return TYPE.ERROR
                if(v.type != TYPE.TYPEBOOL):
                    return TYPE.ERROR
        return Value(None, TYPE.NOTHING, self.row, self.col)