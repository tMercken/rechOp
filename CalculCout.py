#!/usr/bin/python
# -*-coding:Latin-1 -*

import os
from TraiterFileAbsolu import *
from Client import *
from RandomGen import *

tempsSimulation = 960
nbStationMin = 4

def CalculCout (nbStation, tabCout):
    
    #init
    tabStation = [Client()]*nbStation
    fileAbsolu = []
    fileEjecte = []
    fileOrdinaire = []
    temps = 0
    
    while(temps < tempsSimulation):
        #première partie: s'occuper de m'arriver des clients
        arriveeClient = GenerateArriveeRandom()        
        putClientInFile(fileAbsolu, fileOrdinaire, arriveeClient)
        
        #ensuite, triez station et fileAbsolue puis mettre les clients dedans
        tabStation.sort(key = lambda client: client.dureeService)
        fileAbsolu.sort(key = lambda client: client.dureeService)
        
        if (fileAbsolu):
            TraiterFileAbsolu(nbStation, tabStation, fileAbsolu, fileEjecte)
        
        TraiterFileOrdinaire()
        
        #calculCout
        cumOrdinaire = fileOrdinaire.Length() + fileEjecte.Length()
        coutStat = GetCoutStation(tabStation)
        tabCout[nbStation - nbStationMin] += cumOrdinaire*25/60 + fileAbsolu *40/60 + coutStat
        
        temps += 1
        
        
    
def putClientInFile(fileAbsolu, fileOrdinaire, arriveeClient):
    nbAbsolu = GenerateAbsolu(arriveeClient)
    nbOrdinaire = arriveeClient - nbAbsolu
    
    i = 0
    while i < nbAbsolu:
        dureeServ = generateDS()
        fileAbsolu.append(dureeServ, True)
        i += 1
    
    i = 0
    while i < nbOrdinaire:
        dureeServ = generateDS()
        fileOrdinaire.append(dureeServ, False)
        i += 1
        
    
def GetCoutStation(tabStation):
    i = 0
    cout = 0
    for station in tabStation:
        if station.dureeService <= 0:
            cout += 20/60
            
        else:
            if station.isAbsolu:
                cout += 40/60
                
            else:
                cout += 25/60
                
            cout += 35/60
            
        
    
    return cout
                
        
        
    
    
    
       
