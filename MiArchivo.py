"""
	Importacion de la libreria codecs para evitaar conflicto con caracteres especiales
"""
import codecs
"""
Creamos una clase para la lectura de una fichero
"""
class ReadFichero:
	"""
	Inicialisamos la clase abriendo el archivo en la ubicacion establecidad
	"""
	def __init__(self):
		self.archivo=codecs.open("datos.txt", "r")#Usamos open para abrir el fichero(ruta, y r para leer (read)

	"""
	Obtenemos la informacion del fichero y cada linea sera una posicion de un arreglo
	"""
	def obtener_informacion(self):
		return self.archivo.readlines()
	"""
	Cerrramos y Guardamos el Archivo
	"""	
	def cerrar_archivo(self):
		self.archivo.close()