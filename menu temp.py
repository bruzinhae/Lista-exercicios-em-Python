# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 



print ("Menu de temperaturas")
print ("\n")
print ("_"*30)
print ("\n")


af1 = input ("Digite a aferição a temperatura a ser convertida: ")
temp = float (input ("Digite o valor da temperatura a ser convertido: "))

#celsius
if af1 == "celsius" :
    af2 = input ("Digite a aferição a temperatura para que deve ser convertida: ")

    if af2 == "farenheint" :
        conv = (9*temp + 32)/5
        print ("A temperatura convertida é: ", conv, "°F")

    if af2 == "kelvin":
        conv = temp + 273.15
        print ("A temperatura convertida é: ", conv, "°K")

    if af2 == "réamur":
        conv = (temp * 4)/5
        print ("A temperatura convertida é: ", conv, "°Re")

    if af2 == "rankine":
        conv = ((temp+273.15) * 9)/5

        print ("A temperatura convertida é: ", conv, "°Ra")

#farenheint

if af1 == "farenheint" :
    af2 = input ("Digite a aferição a temperatura para que deve ser convertida: ")

    if af2 == "celsius" :
        conv = (5*(temp-32))/9
        print ("A temperatura convertida é: ", conv)

    if af2 == "kelvin":
        conv = ((temp + 459.67) * 5)/9
        print ("A temperatura convertida é: ", conv, "°C", "°K")

    if af2 == "réamur":
        conv = (temp * 9)/4 + 32
        print ("A temperatura convertida é: ", conv, "°Re")

    if af2 == "rankine":
        conv = temp +459.67

        print ("A temperatura convertida é: ", conv, "°Ra")

#Kelvin 

if af1 == "kelvin" :
    af2 = input ("Digite a aferição a temperatura para que deve ser convertida: ")

    if af2 == "celsius" :
        conv = temp - 273.15
        print ("A temperatura convertida é: ", conv, "°C")

    if af2 == "farenheint":
        conv = temp * 1.8 - 459.889
        print ("A temperatura convertida é: ", conv, "°F")

    if af2 == "réamur":
        conv = (temp - 273.15) * 0.8
        print ("A temperatura convertida é: ", conv, "°Re")

    if af2 == "rankine":
        conv = temp * 1.8
        print ("A temperatura convertida é: ", conv, "°Ra")

#réamur 

if af1 == "réamur" :
    af2 = input ("Digite a aferição a temperatura para que deve ser convertida: ")

    if af2 == "celsius" :
        conv = (5 * temp)/4
        print ("A temperatura convertida é: ", conv, "°C")

    if af2 == "kelvin":
        conv = (5* temp)/4 + 273.15
        print ("A temperatura convertida é: ", conv, "°K")

    if af2 == "farenheint":
        conv = (temp * 9)/4 + 32
        print ("A temperatura convertida é: ", conv, "°F")

    if af2 == "rankine":
        conv = (temp * 9)/4 + 491.67
        print ("A temperatura convertida é: ", conv, "°Ra")

#Rankine
if af1 == "rankine" :
    af2 = input ("Digite a aferição a temperatura para que deve ser convertida: ")

    if af2 == "celsius" :
        conv = (temp * 5)/9 - 273.15
        print ("A temperatura convertida é: ", conv , "°C")

    if af2 == "kelvin":
        conv = (temp * 5)/9
        print ("A temperatura convertida é: ", conv, "°K")

    if af2 == "farenheint":
        conv = temp - 459.67
        print ("A temperatura convertida é: ", conv, "°F")

    if af2 == "réamur":
        conv = ((temp - 491,67) * 4)/9
        print ("A temperatura convertida é: ", conv, "°Re")


