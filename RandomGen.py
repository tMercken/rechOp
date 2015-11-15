#!/usr/bin/python
# -*-coding:utf-8 -*

import os
import math
import sys

#m = sys.maxint+1.00
m = sys.maxint+1
#2147483648

a = 17
c = 53
x0 = 144.00

global xnArrivee
global xnDuree
global xnAbsolu

xnArrivee = x0
xnDuree = x0
xnAbsolu = x0

def randomGen(xn):
    return ((a * xn + c)%m)

def GenerateArriveeRandom():
    global xnArrivee    
    xnArrivee = randomGen(xnArrivee)
    un = xnArrivee / m
#   
    if(un < 0.08):
        return 0
    else:
        if(un < 0.11):
            return 1
        else:
            if(un < 0.16):
                return 2
            else:
                if(un < 0.68):
                    return 3
                else:
                    if(un < 0.85):
                        return 4
                    else:
                        return 5                    
            
    
def generateDS():
    global xnDuree    
    xnDuree = randomGen(xnDuree)
    unDuree = xnDuree / m    
    
    if(unDuree < 0.03):
        return 1
    else:
        if(unDuree < 0.08):
            return 2
        else:
            if(unDuree < 0.11):
                return 3
            else:
                if(unDuree < 0.28):
                    return 4
                else:
                    if(unDuree < 0.59):
                        return 5
                    else:
                        return 6 
                    
                    

def GenerateAbsolu(arriveeClient):
    global xnAbsolu
    i = 0
    nbAbsolu = 0
    
    while (i < arriveeClient):
        xnAbsolu = randomGen(xnAbsolu)
        yAbsolu = math.floor((xnAbsolu / m) * 10)
        if  (yAbsolu < 2):
            nbAbsolu += 1
            
        i += 1
        
    return nbAbsolu


#i = 0
#mv = 144.00
#while i < 25:
#    mv = randomGen(mv)
#    print (mv / m)
#    i += 1

#while i < 25:
#    print GenerateArriveeRandom()
#    i += 1
    

        

    

