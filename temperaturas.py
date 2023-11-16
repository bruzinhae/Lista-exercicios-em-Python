# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 



print ("Calculadora de temperaturas")
print ("\n")
print ("_"*30)
print ("\n")

fa = float (input ("Digite o valor da temperatura em farenheint para a transfomação em celsius: "))
ke = float (input ("Digite o valor da temperatura em kelvin para a transfomação em celsius: "))
re = float (input ("Digite o valor da temperatura em Réaumur para a transfomação em celsius: "))
ra = float (input ("Digite o valor da temperatura em Rankine para a transfomação em celsius: "))

cf = (5*(fa-32))/9

ck = ke - 273.15

cre = (5 * re)/4

cra = ((5 * ra)/9)-273.15

print ("O valor da conversão de Farenheint para Celsius é: ", cf)
print ("O valor da conversão de Kelvin para Celsius é: ", ck)
print ("O valor da conversão de Réaumur para Celsius é: ", cre)
print ("O valor da conversão de Rankine para Celsius é: ", cra)