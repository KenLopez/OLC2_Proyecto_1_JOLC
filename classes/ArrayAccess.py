from classes.Tipo import TYPE
class ArrayAccess:
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
            if(v.type != TYPE.TYPELIST):
                return TYPE.ERROR
            index = i.execute(main, tabla, scope)
            if(index == TYPE.ERROR):
                return TYPE.ERROR
            if(index.type != TYPE.TYPEINT64):
                return TYPE.ERROR
            if (index.val > len(v.val)):
                return TYPE.ERROR
            if (index.val < 0):
                return TYPE.ERROR
            v = v.val[index.val-1].execute(main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        return v
    
    def get(self, main, tabla, scope):
        v = self.val.execute(main, tabla, scope)
        for i in range(len(self.access)-1):
            if(v == TYPE.ERROR):
                return TYPE.ERROR
            if(v.type != TYPE.TYPELIST):
                return TYPE.ERROR
            index = self.access[i].execute(main, tabla, scope)
            if(index == TYPE.ERROR):
                return TYPE.ERROR
            if(index.type != TYPE.TYPEINT64):
                return TYPE.ERROR
            if (index.val > len(v.val)):
                return TYPE.ERROR
            if (index.val < 0):
                return TYPE.ERROR
            v = v.val[index.val-1].execute(main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        if(v.type != TYPE.TYPELIST):
            return TYPE.ERROR
        index = self.access[len(self.access)-1].execute(main, tabla, scope)
        if(index == TYPE.ERROR):
            return TYPE.ERROR
        if(index.type != TYPE.TYPEINT64):
            return TYPE.ERROR
        if (index.val > len(v.val)):
            return TYPE.ERROR
        if (index.val < 0):
            return TYPE.ERROR
        v = v.val[index.val-1]
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        return v
