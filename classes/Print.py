from classes.Value import Value
from classes.Tipo import TYPE
class Print:
    def __init__(self, val, type, row, col):
        if(val == None):
            self.val = Value('', TYPE.TYPESTRING, TYPE.VALUE, row, col)
        else:
            self.val = val
        self.type = type
        self.row = row
        self.col = col

    def execute(self, main, tabla):
        output = ""
        for i in range(len(self.val)):
            v = self.val[i].execute(main, tabla)
            if(v!=TYPE.ERROR):
                if(v.type == TYPE.TYPEBOOL):
                    output += str(v.val).lower()
                elif(v.type == TYPE.NOTHING):
                    output += "nothing"
                else:
                    output += str(v.val)
            else:
                return TYPE.ERROR
        if self.type == TYPE.FPRINTLN: output += '\n'
        main.newPrint(output)