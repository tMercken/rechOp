#!/usr/bin/python
# -*-coding:utf-8 -*

import os
import math

m = 256.00
a = 17
c = 53
x0 = 144

global xnArrivee
global xnDuree
global xnAbsolu

xnArrivee = x0
xnDuree = x0
xnAbsolu = x0

def randomGen(xn):
    return ((a * xn + c) % m)

def GenerateArriveeRandom():
    global xnArrivee    
    xnArrivee = randomGen(xnArrivee)
    un = xnArrivee / m
#   nbArrivee = math.floor((6 - 0) * un +0)
    nbArrivee = math.floor(6 * un)
    return nbArrivee
    
def generateDS():
    global xnDuree    
    xnDuree = randomGen(xnDuree)
    unDuree = xnDuree / m    
    dureeService = 1 + math.floor(6 * unDuree)
    return dureeService

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



        

    

