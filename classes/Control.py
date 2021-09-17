from classes.Tipo import TYPE
from classes.Value import Value
class Control:
    def __init__(self, val, type, row, col):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        if(self.type == TYPE.BREAK or self.type == TYPE.CONTINUE):
            if (scope.__contains__('FOR') or scope.__contains__('WHILE')):
                return self
        return TYPE.ERROR
            