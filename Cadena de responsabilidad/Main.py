from ManejadorDefault import ManejadorDefault
from ManejadorUno import ManejadorUno
from ManejadorDos import ManejadorDos
from ManejadorTres import ManejadorTres
from ManejadorCuatro import ManejadorCuatro
from ManejadorCinco import ManejadorCinco
from ManejadorSeis import ManejadorSeis
from ManejadorSiete import ManejadorSiete

def main():
	manejadores = []
	manejadores.append(ManejadorUno())
	manejadores.append(ManejadorDos())
	manejadores.append(ManejadorTres())
	manejadores.append(ManejadorCuatro())
	manejadores.append(ManejadorCinco())
	manejadores.append(ManejadorSeis())
	manejadores.append(ManejadorSiete())
	manejadores.append(ManejadorDefault())

	for i in range(len(manejadores) - 1):
		manejadores[i].setSucesor(manejadores[i+1])

	print "Bienvenido al Portal de Suba"
	opc = raw_input("Que ruta necesita?: ")
	manejadores[0].peticionManejador(opc)

main()
