from classes.Value import Value
from classes.Tipo import TYPE

class Relacional:
    def __init__(self, expIzq, expDer, type, row, col):
        self.expIzq = expIzq
        self.expDer = expDer
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla):
        der = self.expDer.execute(main, tabla)
        izq = self.expIzq.execute(main, tabla)
        if(self.type == TYPE.GREATER):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPECHAR):
                    return Value(izq.val > der.val, TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.LOWER):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPECHAR):
                    return Value(izq.val < der.val, TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.GREATEREQUAL):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPECHAR):
                    return Value(izq.val >= der.val, TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.LOWEREQUAL):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPECHAR):
                    return Value(izq.val <= der.val, TYPE.TYPEBOOL, self.row, self.col)
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.EQUAL):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(False, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPESTRING):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(False, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.NOTHING):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPELIST):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val == der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        elif(self.type == TYPE.DIFFERENT):
            if(izq.type == TYPE.TYPEINT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEFLOAT64):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPEBOOL):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPECHAR):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(True, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPESTRING):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(True, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.NOTHING):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            elif(izq.type == TYPE.TYPELIST):
                if(der.type == TYPE.TYPEINT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEFLOAT64):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPEBOOL):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPECHAR):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPESTRING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.NOTHING):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                elif(der.type == TYPE.TYPELIST):
                    return Value(izq.val != der.val, TYPE.TYPEBOOL, self.row, self.col)
                else:
                    return TYPE.ERROR
            else:
                return TYPE.ERROR
        else:
            return TYPE.ERROR