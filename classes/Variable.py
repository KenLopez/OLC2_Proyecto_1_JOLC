from classes.Tipo import TYPE


class Variable:
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        v = tabla.getSymbol(self.id)
        if(v == TYPE.ERROR):
            return TYPE.ERROR
        elif(v == None):
            return TYPE.ERROR
        else:
            if(v.type == TYPE.FUNCTION):
                return TYPE.ERROR
            val = v.execute(main, tabla, scope)
            if(val==TYPE.ERROR or val==None): 
                return TYPE.ERROR
            return val