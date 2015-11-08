#!/usr/bin/python
# -*-coding:Latin-1 -*

import os
from Client import *   
   
def TraiterFileAbsolu (nbStation, tabStation, fileAbsolu, fileEjecte):
    i=0
    while (i<nbStation):
        if fileAbsolu:
            if (tabStation[i].dureeService <= 0):
                InsertAbsolu(i, tabStation, fileAbsolu)
            
            else:
                if (tabStation[i].isAbsolu):
                    j = nbStation-1
                    while(fileAbsolu and j != i):
                        if(tabStation[j].isAbsolu):
                            EjecterClient(j, tabStation, fileEjecte)
                            InsertAbsolu(i, tabStation, fileAbsolu)
                            
                        j -= 1
                    
                
            
        else:
            return
        
        i += 1
                        
    
def InsertAbsolu(i, tabStation, fileAbsolu):    
    tabStation.insert(i, fileAbsolu[0])
    del tabStation[i+1]
    del fileAbsolu[0]
    
    
def EjecterClient(i, tabStation, fileEjecte):  
    fileEjecte.append(tabStation[i])
    
    
    
         
    