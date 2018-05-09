""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorDefault(Manejador):

	#Override
	def peticionManejador(self, opc):
		print "No es una ruta de nuestro servicio"