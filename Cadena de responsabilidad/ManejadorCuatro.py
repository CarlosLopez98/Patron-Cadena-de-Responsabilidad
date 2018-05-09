""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorCuatro(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "F29":
			print "Esta ruta va hasta el Portal Americas"
		else:
			self.sucesor.peticionManejador(opc)