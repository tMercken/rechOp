#!/usr/bin/python
# -*-coding:utf-8 -*

import os
from Client import * 
from TraiterFileOrdinaire import *  
   
def TraiterFileAbsolu (nbStation, tabStation, fileAbsolu, fileEjecte):
    tabStation.sort(key = lambda client: client.dureeService)
    fileAbsolu.sort(key = lambda client: client.dureeService)
    i=0

    while (i < nbStation and tabStation[i].dureeService <= 0 and fileAbsolu):
        if (tabStation[i].dureeService <= 0):
            AjouterClient(tabStation, i, fileAbsolu)

        i += 1

    j = nbStation - 1


    while (j > i and fileAbsolu):
        if(tabStation[j].isAbsolu == False):
            EjecterClient(tabStation, j, fileEjecte)
            AjouterClient(tabStation, j, fileAbsolu)

        j -= 1
        
        

def EjecterClient(tabStation, i, fileEjecte):  
    fileEjecte.append(tabStation[i])
    
    
    
         
    