""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorTres(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "B50":
			print "Esta ruta va hasta el Portal Norte"
		else:
			self.sucesor.peticionManejador(opc)