""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorUno(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "F19":
			print "Esta ruta va hasta Banderas"
		else:
			self.sucesor.peticionManejador(opc)