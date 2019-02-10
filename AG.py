#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:15:17 2018

@author: zaoryliht-kun
"""
import random
from Individuo import Individuo
import sys

class AG:
    poblacion_inicial = []
    poblacion_total = []
    
    def __init__(self, p, kage):
        #definir la ecuacion a alcanzar
        self.hokage = Individuo(kage)
        self.tabla, self.chakra = self.hokage.makeTruthTable(self.hokage.expression)
        #crear la porblacion inicial en base a esta
        self.crearPoblacionInicial(p)
        #self.poblacion_total = self.poblacion_inicial
        self.pi = int(len(self.poblacion_total))
        #self.sortFitness()
        
    """
    Crea la poblacion inicial en base al numero de individuos
    que se ha introducido a la clase.
    """
    def crearPoblacionInicial(self, numero_de_inidividuos):
        #print (self.hokage.getVar())
        for x in range(0, numero_de_inidividuos):
            individuo = Individuo(self.hokage.expression)
            individuo.createRandomexpression()
            self.poblacion_inicial.append(individuo)
            self.poblacion_total.append(individuo)
            
    def sortFitness(self, poblacion=poblacion_total):
        poblacion.sort(key=lambda x: x.getError(self.chakra), reverse=False)
        return poblacion
            
    """
    A partir de la población que se da por parametro, crea una
    nueva poblacion
    """
    def cicloReproductiro(self, poblacionInicial=poblacion_total):
        nuevaGeneracion = self.cruzar(poblacionInicial)
        poblacionFinal = list(poblacionInicial) + list(nuevaGeneracion)
        poblacionFinal = self.seleccionar(poblacionFinal, 15)
        self.sortFitness(poblacionFinal)
        self.poblacion_total = poblacionFinal
        return poblacionFinal
    
    """
    Recibe la poblacion(los genes que hay actualmente)
    regresa la poblacion(los genes que fueron seleccionados
    por la naturaleza del algoritmo)
    """
    def seleccionar(self, poblacion, index):
        #poblacion = self.sortFitness(poblacion)
        poblacion.sort(key=lambda x: x.getLen(), reverse=False)
        for i in range(0,len(poblacion)-index):
            current = poblacion.pop()
            if(self.contains(poblacion, lambda x: str(x.expression) != str(current.expression))):
                poblacion.append(current)
            else:
                poblacion.append(self.mutar(current))
        poblacion = self.sortFitness(poblacion)        
        return poblacion[:len(poblacion)-index]
        #return poblacion
    
    """
    Recibe la poblacion(los genes que se van a cruzar)
    regresa la poblacion de hijos(solo los genes nuevos
    aplicando la mutacion para cada uno de estos.)
    """
    def cruzar(self, poblacion):
        hijos = []
        #poblacion.sort(key=lambda x: x.getLen(), reverse=False)
        #for i, k in zip(poblacion[0::2], poblacion[1::2]): #prueba 1
        for i in(poblacion):#prueba 2
            #k = poblacion[random.randint(0,len(poblacion)-1)]#prueba 2
            k = random.choice(poblacion)
            if(len(i.expression)<len(k.expression)):
                child = i
                ansestro = k
            else:
                child = k
                ansestro = i
            #el padre largo
            #print(ansestro.expression)
            va = ansestro.getVar()
            ansestro = list(ansestro.getAllVar())
            #las letras del padre largo
            #print("---------------------->",str("".join(ansestro)))
            #el padre corto
            #print(child.expression)
            
            newexpresion = ""
            for j in child.expression:
                if(i.containsAny(str(j),str("".join(va))) and len(ansestro)>0):
                    #e = str(ansestro.pop())
                    #index = random.randint(0,len(ansestro)-1)
                    e = ansestro[0]
                    del ansestro[0]
                    #print("si ",str(j)," por", str(e))
                    #echild.replace(str(j), str(e), 1)
                    newexpresion += str(e)
                else:
                    #print("no ",str(j))
                    newexpresion += j
            child.expression = newexpresion
            #print(child.expression)
            if(self.contains(poblacion, lambda x: str(x.expression) == str(child.expression))):
                child = self.mutar(child, 50)
            hijos.append(child)
            #print("-"*50)
        #poblacion = self.sortFitness(poblacion)
        return hijos
    
    def contains(self, list, filter):
        for x in list:
            if filter(x):
                return True
        return False
    
    """
    Muta e (que es el gen que se va a modificar) threshold
    es el umbral de probabilidad para la modificacion
    regresa e(que es el gen mutado)
    """
    def mutar(self, expr, threshold=50):
        #print("ee->",str(e.expression))
        va = expr.getVar()
        ax = list(expr.getAllVar())
        random.shuffle(ax)
        e = list(expr.expression)
        if(threshold>random.randint(0, 100)):
            for i in range(0,len(e)):
                yaporfavor = random.randint(0,100)        
                if(e[i]=='|' and yaporfavor>50):
                    e[i]='&'
                elif(e[i]=='&' and yaporfavor>50):
                    e[i]='|' 
        else:
            for i in range(1,len(e)):
                yaporfavor = random.randint(0,100)        
                if(e[i-1]=='!' and yaporfavor>50):
                    e[i-1]=''
                elif(e[i-1]!='!' and e[i]!='&' and e[i]!='|' and e[i]!='!' and yaporfavor>50):
                    e[i]='!'+e[i]
            if(e[0] != '!' and yaporfavor>50):
                e[0] = '!'+e[0]
        #profe, si esto no funciona me quito la bida
        newexpresion = ""
        for j in (e):
            if(expr.containsAny(str(j),str("".join(va))) and len(ax)>0):
                #e = str(ansestro.pop())
                #index = random.randint(0,len(ansestro)-1)
                e = ax[0]
                del ax[0]
                #print("si ",str(j)," por", str(e))
                #echild.replace(str(j), str(e), 1)
                newexpresion += str(e)
            else:
                newexpresion += j
        newexpresion = "".join((newexpresion))
        for i in va:
            newexpresion = newexpresion.replace(i+"|"+i, i,-1)
            newexpresion = newexpresion.replace(i+"&"+i, i,-1)
        return Individuo(newexpresion)
    
    def remove_duplicates(self, values):
        output = []
        seen = set()
        for value in values:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output
    
        
if __name__ == "__main__":
    #lo que intentaremos reducir
    expresion ="A&!B | A&B | B&C"# "!A&!B&!C&D | !A&!B&C | C&D | A&!B&C&D | A&!B&C&!D"
    g = AG(50, expresion)
    g.poblacion_total = g.poblacion_inicial
    soluciones = []
    print(expresion)
    print("~"*20)
    print ("poblacion inicial")
    print("-"*50)
    for x in range(0,100):
        #g.poblacion_total = g.cicloReproductiro()
        g.cicloReproductiro()
        print("epoca --------------------------------> ", str(x))
        for i in g.poblacion_total:
            i.setY(g.chakra)
            print (i)
            if(i.getError(g.chakra)==0):
                soluciones.append(i)
                print("."*80)
    print("~"*50)
    print("    SOLUCIONES    ")
    soluciones.sort(key=lambda x: x.getLen(), reverse=True)
    soluciones = g.remove_duplicates(soluciones)
    for x in soluciones:
        x.setY(g.chakra)
        print(x)
                #sys.exit()