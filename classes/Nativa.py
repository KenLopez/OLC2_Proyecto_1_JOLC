from classes.Value import Value
from classes.Tipo import *
from classes.Print import convertString
import math


class Nativa:
    def __init__(self, val, type, row, col):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        v = []
        if(self.type == TYPE.UPPERCASE):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if(v.type == TYPE.TYPESTRING):
                    return Value(v.val.upper(), TYPE.TYPESTRING, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.LOWERCASE):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if(v.type == TYPE.TYPESTRING):
                    return Value(v.val.lower(), TYPE.TYPESTRING, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.LOG10):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(math.log10(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.LOG):
            if (len(self.val)==2):
                base = self.val[0].execute(main, tabla, scope)
                v = self.val[1].execute(main, tabla, scope)
                if(((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64))and((base.type == TYPE.TYPEINT64) or (base.type == TYPE.TYPEFLOAT64))):
                    return Value(math.log(v.val, base.val ), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.LOG):
            if (len(self.val)==2):
                base = self.val[0].execute(main, tabla, scope)
                v = self.val[1].execute(main, tabla, scope)
                if(((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64))and((base.type == TYPE.TYPEINT64) or (base.type == TYPE.TYPEFLOAT64))):
                    return Value(math.log(v.val, base.val ), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.SIN):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(math.sin(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.COS):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(math.cos(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.TAN):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(math.tan(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.SQRT):
            if (len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(math.sqrt(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.PARSE):
            if(len(self.val) == 2):
                t = self.val[0].execute(main, tabla, scope)
                s = self.val[1].execute(main, tabla, scope)
                if((t.type == TYPE.VALUETYPE) and (s.type == TYPE.TYPESTRING)):
                    r = 0
                    if(t.val == TYPE.TYPEINT64):
                        try:
                            r = int(s.val)
                            return Value(r, TYPE.TYPEINT64, self.row, self.col)
                        except ValueError:
                            return TYPE.ERROR
                    elif(t.val == TYPE.TYPEFLOAT64):
                        try:
                            r = float(s.val)
                            return Value(r, TYPE.TYPEFLOAT64, self.row, self.col)
                        except ValueError:
                            return TYPE.ERROR
                return TYPE.ERROR
        elif(self.type == TYPE.TRUNCATE):
            if(len(self.val) == 2):
                t = self.val[0].execute(main, tabla, scope)
                v = self.val[1].execute(main, tabla, scope)
                if(((v.type == TYPE.TYPEFLOAT64) or (v.type == TYPE.TYPEINT64)) and t.type == TYPE.VALUETYPE):
                    if(t.val == TYPE.TYPEINT64 or t.val == TYPE.TYPEFLOAT64):
                        return Value(math.trunc(v.val), t.val, self.row, self.col)
            elif(len(self.val)==1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEFLOAT64) or (v.type == TYPE.TYPEINT64)):
                    return Value(math.trunc(v.val), TYPE.TYPEINT64, self.row, self.col)
            return TYPE.ERROR
            
        elif(self.type == TYPE.FFLOAT):
            if(len(self.val) == 1):
                v = self.val[0].execute(main, tabla, scope)
                if((v.type == TYPE.TYPEINT64) or (v.type == TYPE.TYPEFLOAT64)):
                    return Value(float(v.val), TYPE.TYPEFLOAT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.FSTRING):
            if(len(self.val) == 1):
                v = self.val[0].execute(main, tabla, scope)
                o = convertString(v, main, tabla, scope)
                if(o == TYPE.ERROR):
                    return TYPE.ERROR
                return Value(o, TYPE.TYPESTRING, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.TYPEOF):
            if(len(self.val) == 1):
                v = self.val[0].execute(main, tabla, scope)
                t = names.get(str(v.type))
                if(t == None):
                    t = v.type
                return Value(t, TYPE.TYPESTRING, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.LENGTH):
            if(len(self.val) == 1):
                v = self.val[0].execute(main, tabla, scope)
                if(v.type == TYPE.TYPELIST):
                    return Value(len(v.val), TYPE.TYPEINT64, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.PUSH):
            if(len(self.val) == 2):
                arr = self.val[0].execute(main, tabla, scope)
                if(arr == TYPE.ERROR):
                    return TYPE.ERROR
                if(arr.type != TYPE.TYPELIST):
                    return TYPE.ERROR
                v = self.val[1].execute(main, tabla, scope)
                if(v == TYPE.ERROR):
                    return TYPE.ERROR
                arr.val.append(v)
                return Value(None, TYPE.NOTHING, self.row, self.col)
            return TYPE.ERROR
        elif(self.type == TYPE.POP):
            if(len(self.val) == 1):
                v = self.val[0].execute(main, tabla, scope)
                if(v == TYPE.ERROR):
                    return TYPE.ERROR
                if(v.type != TYPE.TYPELIST):
                    return TYPE.ERROR
                p = v.val[len(v.val)-1].execute(main, tabla, scope)
                v.val = v.val[0:-1]
                return Value(p.val, p.type, p.row, p.col)
            return TYPE.ERROR
