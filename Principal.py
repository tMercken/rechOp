import os
from CalculCout import *
from Sortie import *

nbStationMax = 30
nbStationMin = 4
tabCout = [0]*(1 + nbStationMax-nbStationMin)

def main():
    nbStation = nbStationMin

    while nbStation <= nbStationMax :

        CalculCout(nbStation,tabCout)
        nbStation += 1

    
    RechercheMin(tabCout)
    SortirTabCout(tabCout)
    
    
    
main()