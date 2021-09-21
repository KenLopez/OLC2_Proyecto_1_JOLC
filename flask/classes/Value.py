from classes.Tipo import TYPE


class Value:
    def __init__(self, val, type, row, col, typeStruct = TYPE.NOTHING, mutable = True):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
        self.typeStruct = typeStruct
        self.mutable = mutable
            
    
    def execute(self, main, tabla, scope):
        if(self.type == TYPE.TYPELIST):
            for i in range(len(self.val)):
                nv = self.val[i].execute(main, tabla, scope)
                if(nv == TYPE.ERROR):
                    return TYPE.ERROR
                elif(nv.type != TYPE.TYPELIST and nv.type != TYPE.STRUCT):
                    self.val[i] = nv
            return self
        if(self.type == TYPE.STRUCT):
            for i in self.val:
                nv = self.val[i].execute(main, tabla, scope)
                if(nv == TYPE.ERROR):
                    return TYPE.ERROR
                elif(nv.type != TYPE.TYPELIST and nv.type != TYPE.STRUCT ):
                    self.val[i] = nv
                return self
        return Value(self.val, self.type, self.row, self.col )