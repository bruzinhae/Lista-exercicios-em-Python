# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("\n")
print ("Números crescentes")
print ("\n")

n1 = int (input ("Digite o primeiro valor: "))
n2 = int (input ("Digite o segundo valor: "))
n3 = int (input ("Digite o terceiro valor: "))

if (n1 < n2) and (n1 < n3) and (n2 < n3) :
    print ("Ésta em ordem crescente!", n1, n2, n3)

else : 
    print ("Não está em ordem crescente!")
