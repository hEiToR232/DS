


"""
Sintaxe:

while condicao:
    bloco de repetição


"""
import os
os.system("cls")
"""
n = 1
while n <= 10:
    print(n)
    n = n + 1
"""
n = 1
soma = 0
while n != 0:
    n = float(input("Numero (ou 0 para sair): "))
    soma += n
print(f"Soma...: {soma}")
