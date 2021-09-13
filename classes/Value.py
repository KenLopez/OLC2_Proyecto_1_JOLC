class Value:
    def __init__(self, val, type, row, col):
        self.val = val
        self.type = type
        self.row = row
        self.col = col
    
    def execute(self, main, tabla):
        return self