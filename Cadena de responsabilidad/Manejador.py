""" Clases abstracta Manejador """

class Manejador(object):

	def __init__(self):
		self.sucesor = None

	def peticionManejador(self, opc):
		pass

	def getSucesor(self):
		return self.sucesor

	def setSucesor(self, sucesor):
		self.sucesor = sucesor