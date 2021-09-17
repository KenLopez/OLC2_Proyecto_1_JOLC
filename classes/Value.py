from classes.Tipo import TYPE


class Value:
    def __init__(self, val, type, row, col):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
            
    
    def execute(self, main, tabla, scope):
        if(self.type == TYPE.TYPELIST):
            for i in range(len(self.val)):
                nv = self.val[i].execute(main, tabla, scope)
                if(nv == TYPE.ERROR):
                    return TYPE.ERROR
                elif(nv.type != TYPE.TYPELIST):
                    self.val[i] = nv
            return self
        return Value(self.val, self.type, self.row, self.col )