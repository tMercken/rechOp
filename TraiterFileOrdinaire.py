#!/usr/bin/python
# -*-coding:utf-8 -*

def TraiterFileOrdinaire(nbStation,tabStation,fileEjecte,fileOrdinaire):
    tabStation.sort(key = lambda client: client.dureeService)
    fileEjecte.sort(key = lambda client: client.dureeService)
    fileOrdinaire.sort(key = lambda client: client.dureeService)
    
    i = 0
    while i < nbStation:
        if tabStation[i].dureeService <= 0:
            if fileEjecte:
                AjouterClient(tabStation,i,fileEjecte)
            else:
                if fileOrdinaire :
                    AjouterClient(tabStation, i, fileOrdinaire)
            
        
    
        tabStation[i].dureeService -= 1
        i += 1

def AjouterEjecter(tabStation, i, fileEjecte):
    tabStation.insert(i,fileEjecte[0])
    del tabStation[i+1]
    del fileEjecte[0]

def AjouterClient(tabStation, i, fileClient):    
    tabStation.insert(i,fileClient[0])
    del tabStation[i+1]
    del fileClient[0]