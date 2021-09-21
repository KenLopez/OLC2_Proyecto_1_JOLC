from classes.Tipo import TYPE


class Funcion:
    def __init__(self, params, instructions):
        self.params = params
        self.instructions = instructions
        self.type = TYPE.FUNCTION
    
    def execute(self, main, tabla, scope):
        for i in self.params:
            for j in self.params:
                if (i.id == j.id) and (i!=j):
                    return TYPE.ERROR
        return self
        
