from classes.Value import Value
from classes.Tipo import TYPE
class Print:
    def __init__(self, val, type, row, col):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
        if(val == []):
            self.val.append(Value('', TYPE.TYPESTRING, row, col))

    def execute(self, main, tabla, scope):
        output = ""
        for i in range(len(self.val)):
            v = self.val[i].execute(main, tabla, scope)
            if(v==TYPE.ERROR):
                return TYPE.ERROR
            else:
                str = convertString(v, main, tabla, scope)
                if(str == TYPE.ERROR):
                    return TYPE.ERROR
                output += str
        if self.type == TYPE.FPRINTLN: output += '\n'
        main.newPrint(output)
        return Value(None, TYPE.NOTHING, self.row, self.col)

def convertString(v, main, tabla, scope):
    if(v.type == TYPE.TYPEBOOL):
        return str(v.val).lower()
    elif(v.type == TYPE.NOTHING):
        return "nothing"
    elif(v.type == TYPE.TYPELIST):
        o = '['
        for i in v.val:
            val = i.execute(main, tabla, scope)
            if(val == TYPE.ERROR):
                return TYPE.ERROR
            s = convertString(val, main, tabla, scope)
            if(s==TYPE.ERROR):
                return TYPE.ERROR 
            o += s  + ','
        if len(v.val)>0: o = o[0:-1]
        o += ']'
        return o
    else:
        return str(v.val)
