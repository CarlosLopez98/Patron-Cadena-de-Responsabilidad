""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorCinco(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "G30":
			print "Esta ruta va hasta el Portal Sur"
		else:
			self.sucesor.peticionManejador(opc)