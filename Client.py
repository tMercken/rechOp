#!/usr/bin/python
# -*-coding:Latin-1 -*


class Client:
    """client caractérisé par sa durée de service et le fait qu'il soit absolut ou non (boolean)"""

    def __init__(self, DS = 0, typeClient = False):
        self.dureeService = DS
        self.isAbsolu = typeClient
        