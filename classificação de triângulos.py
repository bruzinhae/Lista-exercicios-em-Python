# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("Verfifcação de um triangulo")
print ("\n")
print ("_"*30)

X= float (input ("Digite o valor do lado X do triânglo: "))
Y= float (input ("Digite o valor do lado Y do triânglo: "))
Z= float (input ("Digite o valor do lado Z do triânglo: "))

if (X+Y < Z) or (Y+ Z <X) or (Z + X < Y):
    print ("Os lados não formam um triânglo!")

elif (X == Y) and (Y == Z):

    print ("Seu triângulo é um triângulo equilátero!")

elif (X == Y) or (Y == Z) or (X == Z):

    print ("Seu triânglo é um Triangulo Isósceles")

elif (X != Y) or (Y != Z) or (X != Z):

    print ("Seu triânglo é um Triangulo Escaleno!")


