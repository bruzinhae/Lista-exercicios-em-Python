# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

#senha pré cadastrada: puccamp123

print ("Calculadora de médias escolares")
print ("\n")
print ("_"*30)
print ("\n")

n1 = float (input ("Digite o valor da nota 1: "))
n2 = float (input ("Digite o valor da nota 2: "))

print ("\n")
print ("_"*30)
print ("\n")

p1 = float (input ("Digite o valor do peso da nota 1: "))
p2 = float (input ("Digite o valor do peso da nota 2: "))

md = ((n1 * p1)+(n2 * p2))/(p1+p2)

if md < 5 :
    print ("REPROVADO!")

elif md >= 5 :
    print ("APROVADO!")

elif (md >= 8) and (md < 9) :
    print ("PARABÉNS SEU DESEMPENHO FOI MUITO BOM!")

elif md > 9 :
    print ("PARABÉNS VOCÊ FOI AORIVADO COM LOUVOR!")

    
