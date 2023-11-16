# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("\n")
print ("Boletim escolar")
print ("_"*30)
print ("\n")

aval1 = float (input ("Digite a nota da Avaliação 1: "))
aval2 = float (input ("Digite a nota da Avaliação 2: "))
presença = float (input ("Digite a porcentagem de presença do aluno: "))

med = ((aval1*5)+(aval2*5))/10

if presença < 75:
    print ("Reprovado!")

elif presença >= 75 and (presença <= 100) and (med <= 4) :
    print ("Reprovado!")
    
elif presença >= 75 and (presença <= 100) and (med > 4) and (med < 6) :
    print ("Exame!")

elif presença >= 75 and (presença <= 100) and (med >= 6) and (med <= 10) :
    print ("Exame!")

