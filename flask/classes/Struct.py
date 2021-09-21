from classes.Tipo import TYPE

class Struct:
    def __init__(self, attributes, mutable, type):
        self.attributes = attributes
        self.mutable = mutable
        self.type = type
    
    def execute(self, main, tabla, scope):
        if(self.type == TYPE.STRUCTDEF):
            for i in self.attributes:
                for j in self.attributes:
                    if (i.id == j.id) and (i!=j):
                        return TYPE.ERROR
            return self