from classes.Value import Value
from classes.Tipo import TYPE
class StructAccess:
    def __init__(self, val, access, row, col):
        self.val = val
        self.access = access
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        v = self.val.execute(main, tabla, scope)
        for i in self.access:
            if(v == TYPE.ERROR):
                return TYPE.ERROR
            if(v.type != TYPE.STRUCT):
                return TYPE.ERROR
            if(v.val.get(i)) == None:
                return TYPE.ERROR
            v = v.val[i].execute(main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        return v
    
    def get(self, main, tabla, scope):
        v = self.val.execute(main, tabla, scope)
        if(isinstance(v, Value)):
            if(not v.mutable):
                return TYPE.ERROR
        for i in range(len(self.access)-1):
            if(v == TYPE.ERROR):
                return TYPE.ERROR
            if(v.type != TYPE.STRUCT):
                return TYPE.ERROR
            if(v.val.get(i)) == None:
                return TYPE.ERROR
            v = v.val[i].execute(main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        if(v.type != TYPE.TYPELIST):
            return TYPE.ERROR
        if(v.val.get(self.access[len(self.access)-1])) == None:
            return TYPE.ERROR
        v = v.val[self.access[len(self.access)-1]]
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        return v