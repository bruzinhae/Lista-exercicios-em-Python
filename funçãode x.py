# -*- coding: utf-8 -*-
"""

@author: 23007950
"""
#Aluna:Bruna Barbour Fernandes 

print ("\n")
print ("Calculadora da função")
print ("_"*30)
print ("\n")

x = int (input ("Digite o valor de X: "))

if x == 0 :
    print ("Não é possível realizar o cálculo!")

elif x != 0 :
        
    fx = (4*((x^2) - 3*(x+9)))/x

    print ("O valor da função de x é: ", fx)

