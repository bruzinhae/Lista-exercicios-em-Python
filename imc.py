# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("\n")
print ("Calculadora de IMC")
print ("\n")

print ("_"*30)

peso= float (input("Digite seu peso: "))
altura = float (input("Digite sua altura: "))

imc= peso/(altura*altura)


if imc < 18.5:
    
    print ("Classificação: Baixo Peso")
    
if imc >= 18.5 and imc <= 24.9:
    
    print ("Classificação: Normal")
    
if imc >= 25 and imc <= 24.99:
    
    print ("Classificação: Sobrepeso")
    
if imc >= 30:
    
    print("Classificação: Obesidade")
    
    