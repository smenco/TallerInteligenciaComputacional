# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:16:47 2022

@author: smenco
"""
"""""PUNTO 1"""
Donacion = float(input("Ingrese la donacion"))

admin = Donacion * 0.35
sist = admin * 0.25
telec = sist * 0.10
cont = Donacion - admin - sist - telec

print("la donacion para telecomunicacion es",telec)
print("La donacion para sistemas es",sist)
print("La donacion para administracion es",admin)
print("La donacion para contabilidad es",cont)