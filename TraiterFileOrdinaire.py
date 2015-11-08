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
                AjouterEjecter(tabStation,i,fileEjecte)
            else:
                AjouterOrdinaire(tabStation, i, fileOrdinaire)
            
        
    
        tabStation[i].dureeService -= 1
        i += 1

def AjouterEjecter(tabStation, i, fileEjecte):
    tabStation.insert(i,fileEjecte[0])
    del tabStation[i+1]
    del fileEjecte[0]

def AjouterOrdinaire(tabStation, i, fileOrdinaire):
    if fileOrdinaire :
        tabStation.insert(i,fileOrdinaire[0])
        del tabStation[i+1]
        del fileOrdinaire[0]