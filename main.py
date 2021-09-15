from classes.Value import Value
import analizador.gramatica as g
from classes.Tipo import TYPE
from classes.Aritmetica import Aritmetica
from classes.Global import Global

f = open("./analizador/prueba2.txt", "r")
input = f.read()

main = Global()
main.instrucciones = g.parse(input)
main.execute()
print(main.output)