#!/usr/bin/python
# -*-coding:Latin-1 -*

import os

class Client:
    """client caractérisé par sa durée de service et le fait qu'il soit absolut ou non (boolean)"""

    def __init__(self, DS = 0, type = False):
        self.dureeService = DS
        self.isAbsolu = type
        