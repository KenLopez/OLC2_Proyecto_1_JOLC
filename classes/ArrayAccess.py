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
            v = self.getAccess(v.val, index.val, main, tabla, scope)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        return v
    

    def getAccess(self, arr, pos, main, tabla, scope):
        if (pos > len(arr)-1):
            return TYPE.ERROR
        if (pos < 0):
            return TYPE.ERROR
        return arr[pos].execute(main, tabla, scope)
