""" Clase que hereda de Manejador """

from Manejador import Manejador

class ManejadorDos(Manejador):

	#Override
	def peticionManejador(self, opc):
		if opc == "H15":
			print "Esta ruta va hasta el Portal Tunal"
		else:
			self.sucesor.peticionManejador(opc)