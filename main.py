import analizador.gramatica as g

f = open("./analizador/prueba.txt", "r")
input = f.read()

instrucciones = g.parse(input)