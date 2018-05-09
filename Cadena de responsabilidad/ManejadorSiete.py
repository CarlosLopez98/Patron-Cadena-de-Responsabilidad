""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorSiete(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "H17":
			print "Esta ruta va hasta el Portal Usme"
		else:
			self.sucesor.peticionManejador(opc)