""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorSeis(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "J73":
			print "Esta ruta va hasta Universidades"
		else:
			self.sucesor.peticionManejador(opc)