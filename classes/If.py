from classes.Value import Value
from classes.Tipo import TYPE
class If:
    def __init__(self, conditions, instructions, elseinstructions, row, col):
        self.conditions = conditions
        self.instructions = instructions
        self.elseinstructions = elseinstructions
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        nscope = scope+"_IF"
        for i in range(len(self.conditions)):
            res = self.conditions[i].execute(main, tabla, nscope)
            if(res==TYPE.ERROR):
                return TYPE.ERROR
            elif(res.type!=TYPE.TYPEBOOL):
                return TYPE.ERROR
            elif(res.val):
                for j in self.instructions[i]:
                    res2 = j.execute(main, tabla, nscope)
                    if(res2 == TYPE.ERROR):
                        return TYPE.ERROR
                return Value(None, TYPE.NOTHING, self.symbol.row, self.symbol.col)
        for i in self.elseinstructions:
            res = i.execute(main, tabla, nscope)
            if(res == TYPE.ERROR):
                return TYPE.ERROR
        return Value(None, TYPE.NOTHING, self.symbol.row, self.symbol.col)
