# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:40:52 2022

@author: smenco
"""
"""Punto2"""

persona1 = float(input("Ingrese la cantidad de la primera persona"))
persona2 = float(input("Ingrese la cantidad de la segunda persona"))
persona3 = float(input("Ingrese la cantidad de la tercera persona"))



total = persona1 + persona2 + persona3

porcentaje1 = total // persona1
porcentaje2 = total // persona2
porcentaje3 = total // persona3

print("El valor total es",total)
print("El porcentaje de la persona 1 fue",porcentaje1)
print("El porcentaje de la persona 2 fue",porcentaje2)
print("El porcentaje de la persona 3 fue",porcentaje3)