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

    def execute(self, main, tabla):
        output = ""
        for i in range(len(self.val)):
            v = self.val[i].execute(main, tabla)
            if(v!=TYPE.ERROR):
                output += self.convertString(v)
        if self.type == TYPE.FPRINTLN: output += '\n'
        main.newPrint(output)

    def convertString(self, v):
        if(v.type == TYPE.TYPEBOOL):
            return str(v.val).lower()
        elif(v.type == TYPE.NOTHING):
            return "nothing"
        else:
            return str(v.val)
