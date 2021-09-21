class Symbol:
    def __init__(self, id, val, scope, row, col):
        self.id = id
        self.val = val
        self.scope = scope
        self.row = row
        self.col = col
    
    def execute(self, main, tabla, scope):
        return self.val