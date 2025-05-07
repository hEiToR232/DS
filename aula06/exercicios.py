import os
os.system("cls")

#Exercicios:
# 1 - Crie uma função que passe dois valores por parâmetro e exiba o de maior valor
def maiorvalor(n1:int , n2:int) -> int:
    if n1>n2:
        return n1
    else:
        return n2
# 2 - Crie uma função que passe três valores por paramêmetro e exiba o de menor valor
def menorvalor(n1: int, n2: int, n3: int) -> int:
    menor = n1
    if menor > n2:
        menor = n2
    elif menor > n3:
        menor = n3
    return menor    
# 3 - Crie um procedimento que passe um valor por parâmentro e exiba em ordem decrescente até 0
def decrescente(n: int) -> None:
    for i in range (n, -1, -1):
        print(i)
print("Exercicio1: ")
ex1 = maiorvalor(12, 23)
print(ex1)
print()
print("Exercicio2: ")
ex2 = menorvalor(32, 54, 10)
print(ex2)
print()
print("Exercicio3: ")
decrescente(10)

# Faça uma rotina onde o usuario digite 5 elementos em uma lista
os.system("cls")
def preenche_lista(l: list) -> None:
    for i in range(5):
        elem = input("Elemento: ")
        l.append(elem)

lista=[]
preenche_lista(lista)
# Faça uma função que retorne a quantidade de elementos inteiros contidos numa lista
c = 0 
for i in range(5):
    x = lista[i].isnumeric()
    if x == True:
        c += 1
print(c)