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
        ntabla = SymbolTable(tabla)
        v = self.condition.execute(main, ntabla, nscope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        if(v.type != TYPE.TYPEBOOL):
            return TYPE.ERROR
        while v.val:
            for i in range(len(self.instructions)):
                res = self.instructions[i].execute(main, ntabla, nscope)
                if(res == TYPE.ERROR):
                    return TYPE.ERROR
            v = self.condition.execute(main, ntabla, nscope)
            if(v == TYPE.ERROR):
                return TYPE.ERROR
            if(v.type != TYPE.TYPEBOOL):
                return TYPE.ERROR
        return Value(None, TYPE.NOTHING, self.row, self.col)