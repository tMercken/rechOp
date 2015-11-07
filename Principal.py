import os
from CalculCout import *
from Sortie import *

nbStationMax = 30
nbStation = 4
tabCout = [0]*nbStationMax

def main():
	
	while nbStation < nbStationMax :
		CalculCout(nbStation,tabCout)
		nbStation += 1

	RechercheMin(tabCout)
	SortirTabCout(tabCout)
