import analizador.gramatica as g
from classes.Global import Global
import sys
sys.setrecursionlimit(4000)

f = open("./analizador/prueba7.txt", "r")
input = f.read()

main = Global()
main.instrucciones = g.parse(input)
main.execute()
print(main.output)