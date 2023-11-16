# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

#senha pré cadastrada: puccamp123

print ("Validação de numero par ou ímpar ")
print ("\n")
print ("_"*30)
print ("\n")

num = int (input ("Digite o número a ser verificado: "))

cal = num % 2 

if cal == 0 :
    print ("O número é par!")
else : 
    print ("O número é ímpar!")
