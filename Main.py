from MiArchivo import * # importamos los ficherosn nescesarios para ejecutar
from MiModelo import *

f = ReadFichero() # Creamos una variable con el obejto leer fichero

lista = f.obtener_informacion() # Guardamso toda la lista de obtener informacion en la variable lista
lista =[l.split(",") for l in lista] # Separamos cada elemento de cada linea(l) por el caracter (,)
lista_numeros=[] # creamos una lista auxiliar
for linea in lista: # recorremso cada linea
	for numero in linea: # recorremos cada numero en cada linea
		lista_numeros.append(int(numero)) # En la lsita auxiliar guardamos cada numero pero ahora trasformado en tipo entero
arrBin= ArrregloBinario(lista_numeros) # llamamos al costructor de la clase arregloBinario y le damos como entrada la lista obtenida del txt
print(arrBin) # imprimimos nuestra lista(Recordar personalizar el str y que el cosntructor ordenene el arreglo)
if arrBin.busquedaBinaria(3)!= -1: # si busqueda binario devuelve un numero diferente a -1 	imprime un mensaje con la posicion del elemento buscado
	print("El entero %d se encuentra en la posicion %d"%(3,arrBin.busquedaBinaria(3)))
else: # si no cumple la primera condicion no ha encontrado el elemento e imprime un mensaje para ello 
	print("No se ha encontrado el elemento buscado")

