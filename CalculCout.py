#!/usr/bin/python
# -*-coding:utf-8 -*

import os
from TraiterFileAbsolu import *
from Client import *
from RandomGen import *
from TraiterFileOrdinaire import *

tempsSimulation = 960
nbStationMin = 4

def CalculCout (nbStation, tabCout):
    
    #init
    tabStation = [Client(-1, False)]*nbStation
    fileAbsolu = []
    fileEjecte = []
    fileOrdinaire = []
    temps = 0
    
    while(temps < tempsSimulation):
        #première partie: s'occuper de m'arriver des clients
        arriveeClient = GenerateArriveeRandom()       
        putClientInFile(fileAbsolu, fileOrdinaire, arriveeClient)
        
        if (fileAbsolu):
            TraiterFileAbsolu(nbStation, tabStation, fileAbsolu, fileEjecte)
        
        TraiterFileOrdinaire(nbStation, tabStation, fileEjecte, fileOrdinaire)
        
        #calculCout
        cumOrdinaire = len(fileOrdinaire) + len(fileEjecte)
        coutStat = GetCoutStation(tabStation)
        tabCout[nbStation - nbStationMin] += cumOrdinaire * (float(25)/60) + len(fileAbsolu) * (float(40)/60) + coutStat
        
        temps += 1
        
        
    
def putClientInFile(fileAbsolu, fileOrdinaire, arriveeClient):
    nbAbsolu = GenerateAbsolu(arriveeClient)
    nbOrdinaire = arriveeClient - nbAbsolu
    
    i = 0
    while i < nbAbsolu:
        dureeServ = generateDS()
        fileAbsolu.append(Client(dureeServ, True))
        i += 1
    
    i = 0
    while i < nbOrdinaire:
        dureeServ = generateDS()
        fileOrdinaire.append(Client(dureeServ, False))
        i += 1
        
    
def GetCoutStation(tabStation):
    i = 0
    coutS = 0.0

    while i < len(tabStation):
        if tabStation[i].dureeService <= 0:
            coutS += float(20)/(60)
            
        else:
            if tabStation[i].isAbsolu:
                coutS += float(40)/(60)
                
            else:
                coutS += float(25)/(60)                
                
            coutS += float(35)/(60)
                 
        
        i += 1
    
    
    
    return coutS
    
    
                
        
        
    
    
    
       
