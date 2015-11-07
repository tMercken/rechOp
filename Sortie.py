#!/usr/bin/python
# -*-coding:utf-8 -*

import os
from CalculCout import nbStationMin  

def RechercheMin (tabCout):
    minimum = min(tabCout)
    indMin = tabCout.index(min(tabCout))    

    fSortie = open('Sortie.txt','w')
    
    fSortie.write("Coût minimal: ")
#    fSortie.write(minimum)
    print >>fSortie, minimum
    fSortie.write('\n')
    
    bestNbStation = nbStationMin + indMin
    fSortie.write('Nombre de station le plus économique: ')
#    fSortie.write(bestNbStation)
    print >>fSortie, bestNbStation
    fSortie.write('\n')
    
    fSortie.close()


def SortirTabCout(tabCout):
    fSortie = open('Sortie.txt','a')
    fSortie.write('\n')
    i = 0
    
    while i < len(tabCout):
        fSortie.write('nombre de Station: ')
        print >>fSortie, nbStationMin + i
        
        fSortie.write('  cout : ')
        print >>fSortie, tabCout[i]
        fSortie.write('\n')
        i += 1
    
    fSortie.close()
    

        