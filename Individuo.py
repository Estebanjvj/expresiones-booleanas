#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:39:15 2018

@author: zaoryliht-kun
"""
from K import K
import random

class Individuo(K):
    
    def __init__(self, expression):
        self.expression = expression
        
    def setY(self, y):
        self.y = y
    
    '''
    Obtiene todas las variables que tiene la expression [A,B,C,...,Z]
    '''
    def getVar(self):
        return self.getVariables(self.expression)
    
    '''
    Obtiene el tamaño de la expression contando cuantas variables hay y cuantas
    veces estan, P.E. 'A|B|C|!C&B' = 5, 'A&!A' = 2
    '''
    def getLen(self):
        return int(len(self.getVariables(self.expression, False)))
    
    '''
    Obtiene las variables hay y cuantas
    veces estan, P.E. 'A|B|C|!C&B' = 5, 'A&!A' = 2
    '''
    def getAllVar(self):
        return (self.getVariables(self.expression, False))
    
    def containsAny(self, str, set):
        #Check whether 'str' contains ANY of the chars in 'set'
        return 1 in [c in str for c in set]
    
    '''
    Muestra la tabla de verdad, entradas y salidas correspondientes a esta
    '''
    def printTruthTable(self):
        self.showTruthTable(self.expression)
        
    def getError(self, y):
        entradas, salidas = self.makeTruthTable(self.expression)
        if(len(y)==len(salidas)):
            err=0
            for r, f in zip(y, salidas):
                if(r!=f):
                    err += 1
            err = err/len(y)*100
            #print(err)
            #print (salidas, y)
            return err
        else:
            return 100
    
    '''
    Basandose en la expression actual, convierte esta misma en otra de manera
    aleatoria, que sea igual o menor al numero de variables que tiene y que
    tenga al menos una vez cada variable.
    '''
    def createRandomexpression(self):
        #lista de variables
        var = list(self.getVar())
        #lista de variables (obligatorias desordenadas)
        var_ob = list(self.getVar())
        random.shuffle(var_ob)
        #operadores aritmeticos ['|','&']
        #actual expression booleana aleatoria
        cur = [];
        #maximo de variables que puede haber no debe ser mayor a la ecuacion
        #original
        maximo = random.randint(int(len(self.getVar()))+1,self.getLen())
        for i in range(0,maximo-1):
            #negativo
            if(random.randint(0,100)<50):
                cur += '!'
            #si aun no han pasado todas las variables al menos una vez
            if(var_ob):
                cur += var_ob.pop()
            else:
                cur += var[random.randint(0,len(var)-1)]
            #operador aritmetico
            if(random.randint(0,100)<50):
                cur += '|'
            else:
                cur += '&'
        #para cerrar el ultimo operdor aritmetico                
        cur += var[random.randint(0,len(var)-1)]
        expression = "".join(cur)
        self.expression = expression
        #print(expression)
        return expression
    
    def __str__(self):
        return ("".join(str(self.getError(self.y))+" : "+self.expression))

if __name__ == "__main__":
    #expression = "!A&!B&!C&D | !A&!B&C | C&D | A&!B&C&D | A&!B&C&!D"
    expression = "A&!B | A&B | B&C"
    print("Original: ",expression)
    k = Individuo(expression)
    k.showTruthTable(expression)
    en, sa = k.makeTruthTable(expression)
    print("~"*50)
    
    #ex = "!B&C|C&D|!A&!B&D"
    #ex = "A|B|C&D"
    ex = "A|B&C&B"
    print("No original ",ex)
    j = Individuo(ex)
    j.showTruthTable(ex)
    print("~"*50)
    print(str(j.getError(sa)))
    #k.createRandomexpression()
