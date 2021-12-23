from Formas import Forma
import random

class Controla:
    forma1 =     [[0,0,0],
                 [1,1,1],
                 [0,0,0]]

    forma2 =    [[0,0,0],
                [1,1,1],
                [0,1,0]]

    formas = []

    formasNaTela = []
    
    colunasPreenchidas = []


    def __init__(self) -> None:
        self.formas.append(self.forma1)
        self.formas.append(self.forma2)
        self.formasNaTela = []

    def criaForma(self, indice):
        self.formasNaTela.append(Forma(0,10,self.formas[indice]))

    def renderFormas(self, lib, tela):
        for i in self.formasNaTela:
            for j in i.partes:

                lib.draw.rect(tela,[255,0,0],[j.x,j.y,30,30])

    def down(self):
        for i in self.formasNaTela:
            i.down()
            



