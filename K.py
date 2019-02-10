#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:57:45 2018

@author: zaoryliht-kun
"""
import itertools

class K():
    def __init__(self):
        pass
    
    ''' suscessfull!!
    Segun la expresion dada, cuenta las letras distintas (A, B C, D, ..., Z)
    ignorando los signos [&],[ ],[|],[(],[)],[!]:
        
    Recibe la expresion boleana
    Regresa las entradas
    '''
    def getVariables(self, expresion, setted=True):
        #convert upper case
        
        if(setted):
            curr = ''.join(set(expresion.upper()))
        else:
            curr = ''.join((expresion.upper()))
        #delete + and . characters
        curr = curr.replace("&", "")
        curr = curr.replace("|", "")
        curr = curr.replace(" ", "")
        curr = curr.replace("!", "")
        curr = curr.replace("(", "")
        curr = curr.replace(")", "")
        #print (curr)
        if(setted):
            return ''.join(sorted(curr))
        else:
            return ''.join((curr))
    
    '''
    Segun las etradas y expresion dadas, este metodo intentara devolver el
    valor binario correspondeinte al resultado de cada una de las operaciones
    binarias en la expresion:
        
    Recibe expresion boleana
    Recibe entradas para cada variable
    Regresa el resultado de la expresion
    '''
    def resolverEcuacion(self, expresion, entradas):
        real = expresion
        real = real.upper()
        for i in entradas:
            # mayusculas 1
            real = real.replace(str(i),str(entradas.get(i)))
            #print ("Se reemplazó "+ str(i)+ " por "+str(entradas.get(i)))
            #minusculas 0
            #real = real.replace(str(i.lower()),str(int(not entradas.get(i))))
        real = real.replace(" ", "")
        real = real.replace("&", " and ")
        real = real.replace("|", " or ")
        real = real.replace("!", " not ")
        #print (real)
        return eval(real)
    
    '''
    Segun la expresion dada, este metodo se encargara de crear todas las com-
    binaciones posibles de 0s y 1s entre las variables que tenga esta.
    Posteriormente se analizará la tabla de verdad y se calculará la expresion
    boleana para obtener sus respuestas:
    
    Recibe expresion boleana
    '''
    def makeTruthTable(self, expresion):
        var = self.getVariables(expresion)
        y = []
        #print(str(list(var))+",Out")
        #print('-'*len(var)*5)
        table = list(itertools.product([1,0], repeat=len(var)))
        for i in (table):
            entradas = {}
            for index, j in enumerate(i):
                #print (str(i[index])+" "+str(var[index]))
                entradas[var[index]] = i[index]
            #print (entradas)
            x = self.resolverEcuacion(expresion, entradas)
            #print("|"+str((i))+" | "+str(x)+" |")
            y.append(int(x))
        #print('-'*len(var)*5)
        return table, y
    
    def showTruthTable(self, expresion):
        var = self.getVariables(expresion)
        table, output = self.makeTruthTable(expresion)
        print("["+', '.join(var)+"] OUT")
        print('-'*len(var)*4)
        for t, o in zip(reversed(table), reversed(output)):
            print(list(t),o)
        
    
    def main(self):
        #expresion = "a&B | A&B"
        #expresion = "A&B&c&d | A&b&c&d | A&B&C&d | A&b&C&D | A&b&C&d"
        expresion = "!A&!B&!C&D | !A&!B&C | C&D | A&!B&C&D | A&!B&C&!D"
        self.showTruthTable(expresion)
        #print (expresion)
        #for i in out:
            #print (i)
        
if __name__ == "__main__":
    k = K()
    k.main()