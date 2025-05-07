#apaga a tela
import os
os.system("cls")

valor = 10 #int
print(valor, type(valor))
valor = "OW MY GOG" # str
print(valor, type(valor))
valor = 15.6 # float
print(valor, type(valor))
valor = True # bool
print(valor, type(valor))

"""
Operadores Aritméticos
+ - * /
// divisão inteira
% módulo (resto da divisão)
"""
os.system("cls")
resp = 10 // 3
print(resp)
resp = 13.5 % 3
print(resp)
"""
print() => Saída de dados [printf da linguagem C]
input() => Entradade dados [scanf da linguagem C] 
"""
os.system("cls")

#valor = input("Digite: ")
print(valor)

# exercicio
# Dado um numero pelo usuario, mostrar o seu dobro
os.system("cls")

#o input é string
#valor = int(input("Digite: "))
#casting da variavel valor
dobro = valor * 2
print(dobro,type(dobro))
os.system("cls")


# exercicios
"""
1. Dado um valor float pelo usuario que representa uma temperatura em celsius, converta para farenheigth [sic]
2. Faça o contrario do anterior
3.  dada uma quantia, informe quantas cédulas de 100, 50, 20 e 10 são necessarias para compor este valor
"""
#1
os.system("cls")

#tempC = float(input("Digite a temperatura em graus Celsius: "))
#tempF = (1.8 * tempC) + 32
#print(tempF)

#2
os.system("cls")

#tempF = float(input("Digite a temperatura em graus Fahrenheit: "))
#tempC = (tempF - 32) / 1.8
# print(tempC)

#3
os.system("cls")

valor = int(input("Digita o dindin: "))
dcem = valor // 100
valor %= 100
print(dcem)
dcinquenta = valor //50
valor %= 50
print(dcinquenta)
dvinte = valor //20
valor %= 20
print(dvinte)
ddez = valor // 10
valor %= 10
print(ddez)