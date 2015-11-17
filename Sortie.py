#!/usr/bin/python
# -*-coding:utf-8 -*

import os
#from CalculCout import nbStationMin  
nbStationMin = 4

def RechercheMin (tabCout):
    minimum = min(tabCout)
    indMin = tabCout.index(min(tabCout))    

    fSortie = open('SortieCout.txt','w')
    
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
    fSortie = open('SortieCout.txt','a')
    fSortie.write('\n')
    i = 0
    
    while i < len(tabCout):
        fSortie.write('nombre de Station: ')
        print >>fSortie, nbStationMin + i
        
        fSortie.write('  cout : ')
        print >>fSortie,tabCout[i]
        fSortie.write('\n')
        i += 1
        
    fSortie.close()

def InitFichierSortirStation():
    fSortieStation = open('SortieStation.txt','w')
    fSortieStation.close()

def SortirNbStation(nbStation):
    fSortieStation = open('SortieStation.txt','a')
    fSortieStation.write('\n')

    fSortieStation.write("nombre de station :")
    print >> fSortieStation, nbStation

    fSortieStation.close()

def SortirArriveeClient(arriveeClient):
    fSortieStation = open('SortieStation.txt','a')
    fSortieStation.write('\n')

    fSortieStation.write("nombre d'arrivee : ")
    print >> fSortieStation, arriveeClient

    fSortieStation.close()
    
def SortirTabStation(tabStation, fileAbsolu, fileOrdinaire, fileEjecte, nbStation):
    fSortieStation = open('SortieStation.txt','a')

    chaineStation = "[ | "
    i = 0
    while (i < nbStation):
        if (tabStation[i].dureeService <= 0):
            chaineStation += "    | "
        else:
            if (tabStation[i].isAbsolu):
                chaineStation += "A"
            else:
                chaineStation += "O"

            chaineStation += " ("
            chaineStation += str(tabStation[i].dureeService)
            chaineStation += ") | "

        i += 1

    chaineStation += "]"
    print >> fSortieStation, ("station :")
    print >> fSortieStation, chaineStation
    fSortieStation.write('\n')

    print >> fSortieStation, ("fileAbsolu : " + str(len(fileAbsolu)))
    print >> fSortieStation, ("fileOrdinaire : " + str(len(fileOrdinaire)))
    print >> fSortieStation, ("fileEjecte : " + str(len(fileEjecte)))

    fSortieStation.close()
        