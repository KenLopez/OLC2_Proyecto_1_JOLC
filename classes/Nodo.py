class Nodo:
    def __init__(self, tag, children = []):
        self.tag = tag
        self.children = children

    def graficar(self, dot):
        if (self.children == []) :
            return 
        else:
            for son in self.children:
                dot.node('nodo'+str(id(son)), son.tag)
                dot.edge('nodo'+str(id(self)), 'nodo'+str(id(son)), constraint='true')
                son.graficar(dot)
            return
