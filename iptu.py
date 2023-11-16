# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("Calculadora de IPTU")
print ("\n")
print ("_"*30)
print ("\n")

anoa = int (input ("Digite o ano atual: "))
anoc = int (input ("DIgite o ano de contrução da sua casa: "))

idade = anoa - anoc 

if idade < 5 :
    print ("Seu percentual de desconto é de 0%")

elif (idade >= 5) and (idade < 20):
    print ("Seu percentual de desconto é de 15%")

elif (idade >= 20) and (idade < 40):
    print ("Seu percentual de desconto é de 25%")

elif idade >= 40:
    print ("Seu percentual de desconto é de 30%")

