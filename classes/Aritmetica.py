from classes.Value import Value
from classes.Tipo import TYPE

class Aritmetica:

    def __init__(self, expIzq, expDer, type, row, col):
        self.expIzq = expIzq
        self.expDer = expDer
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        der = self.expDer.execute(main, tabla, scope)
        if(der==TYPE.ERROR):
            return TYPE.ERROR
        izq = self.expIzq.execute(main, tabla, scope)
        if(izq == TYPE.ERROR):
            return TYPE.ERROR
        if(self.type == TYPE.ADDITION):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val + der.val, TYPE.TYPEINT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val + der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val + der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val + der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.SUBSTRACTION):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val - der.val, TYPE.TYPEINT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val - der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val - der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val - der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.MULTIPLICATION):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val * der.val, TYPE.TYPEINT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val * der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val * der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val * der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR  
            elif(izq.type == TYPE.TYPESTRING):
                if(der.type == TYPE.TYPESTRING):
                    return Value(izq.val + der.val, TYPE.TYPESTRING, self.row, self.col)
                else:
                    return TYPE.ERROR
            else: 
                return TYPE.ERROR      
        elif(self.type == TYPE.DIVISION):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val / der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val / der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val / der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val / der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
        elif(self.type == TYPE.POWER):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(pow(izq.val, der.val), TYPE.TYPEINT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(pow(izq.val, der.val), TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(pow(izq.val, der.val), TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(pow(izq.val, der.val), TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPESTRING):
                if(der.type == TYPE.TYPEINT64):
                    r = ""
                    for _ in range(der.val):
                        r += izq.val
                    return Value(r, TYPE.TYPESTRING, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.MODULUS):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val % der.val, TYPE.TYPEINT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val % der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val % der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val % der.val, TYPE.TYPEFLOAT64, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        else: 
            return TYPE.ERROR