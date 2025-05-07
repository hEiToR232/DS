# Operadores relacionais
# > >= < <= != ==

# Operadores logicos
# not (!) and (&&) or (||)
import os
os.system("cls")
#Decisao Simples
idade = 20
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Decisao encadeada
x = 50
if x < 0:
    print("Negativo")
elif x > 0:
    print("Positivo")
else:
    print("nulo")

#  OU
x = 50
if x <0:
    print("Negativo")
else:
    if x > 0:
        print("Positivo")
    else:
        print("Nulo")

"""
Exercicios:
1. Pesquisar a tabela do INSS 2025 e fazer um programa que 
peguem o salario de um funcionario e informe quanto ele pagara de INSS

2. Pesquisar a tabela de IMPOSTO DE RENDA 2025 e fazer um programa que 
peguem o salario de um funcionario e informe quanto ele pagara de IR

3. Dado o salário de um funcionário, calcular os impostos acima, exibindo os dados da seguinte forma:
-----------------------------------------
Salario bruto....: R$99999,99
INSS.............: R$99999,99
IR...............: R$99999,99
Salário Líquido..: R$99999,99
-----------------------------------------
"""

os.system("cls")
valor = float(input("Digite o seu salario: "))
if valor <= 1518:
    inss = valor * 0.075
elif valor > 1518 and valor <= 2793.88:
    inss = valor * 0.09
elif valor > 2793.88 and valor <= 4190.83:
    inss = valor * 0.12
elif valor > 4190.83 and valor <= 8157.41:
    inss = valor * 0.14
elif valor > 8157.41:
    inss = 951.62

if valor <= 2259.20:
    ir = 0
elif valor > 2259.20 and valor <= 2826.65:
    ir = valor * 0.075
elif valor > 2826.65 and valor <= 3751.05:
    ir = valor * 0.15
elif valor > 3751.05 and valor <= 4664.68:
    ir = valor * 0.225
elif valor > 4664.68: 
    ir = valor * 0.275
sl = valor - (ir + inss) 

print(f"----------------------------------------- \nSalario Bruto.......: {valor} \nINSS................: {inss} \nIR..................: {ir} \nSalario Liquido.....: {sl} \n-----------------------------------------")

os.system("cls")

cpf = int(input("Digite seu CPF: "))
