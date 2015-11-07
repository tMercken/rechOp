import os
from CalculCout import *
from Sortie import *

nbStationMax = 30
nbStationMin = 4
tabCout = [0]*(nbStationMax-nbStationMin)

def main():
    nbStation = nbStationMin
    print 'go'
    while nbStation <= nbStationMax :
        CalculCout(nbStation,tabCout)
        nbStation += 1

    print 'end'
    RechercheMin(tabCout)
    SortirTabCout(tabCout)
    print 'end2'
    
    
main()