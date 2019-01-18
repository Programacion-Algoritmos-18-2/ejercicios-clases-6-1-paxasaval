class ArrregloBinario(object):
	"""docstring for ArrregloBinario"""
	def __init__(self, losdatos): # contructor del arreglo binario recibe una lista
		self.datos = sorted(losdatos) # ordena la lista y la guarda como datos


	def busquedaBinaria(self,elementoBusqueda): # Realizamos la buqueda binaria para ello recibimso el lemento a encontrar
		# inicialisamos las variables auxiliares
		inferior=0
		superior=len(self.datos) - 1
		medio = int((inferior + superior + 1) / 2)
		ubicacion = -1
		while (inferior <= superior) and (ubicacion == -1): # ciclo mientras que se ejecuta hasta encontrar el lemento o hasta q inferios sea mayor a superior
			if elementoBusqueda == self.datos[medio]: # si encuntra el lementno en la posicion del medio ubicacion toma ese valor 
				ubicacion = medio
			elif elementoBusqueda < self.datos[medio]: # si el elemento es menor al elemento en al posicion medio  superior se actualiza
				superior = medio - 1
			else: # si ninguna condicion se cumplio se actualiza inferior
				inferior = medio + 1
			medio = int((inferior + superior + 1) / 2) # Al finalizar los condicionales se actualiza medio
		return ubicacion # devuelvo la ubicacion (caso de no encontrarlo se devuelve -1)

"""
	Personalizamos el metodo str para imprimir nuestro arreglo binario como lo deseemos(una linea sin comas ni corchetes)
"""

	def __str__(self): 
		cadena=""
		for elemento in self.datos:
			cadena = ("%s %d"%(cadena,elemento))
		return cadena




		