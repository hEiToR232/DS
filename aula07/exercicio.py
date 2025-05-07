import os
os.system("cls")
lista = list()
n = ""
def preenche_lista(lista):
    while True:
        n = (input("Digite um elemento: "))
        if n == ".":
            break
        lista.append(n)

def exibe_lista(lista):
    print(lista)

def conta_elementos(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

def retorna_indice(lista, elemento):
    for i in range (conta_elementos(lista)):
        if  lista[i] == elemento:
            return i
    return -1

def busca(lista, elemento):
    cont = 0
    for i in lista:
        if elemento == i:
            cont += 1
    return cont

def conta_inteiro(lista):
    c = 0 
    for i in range (conta_elementos(lista)):
        x = lista[i].isnumeric()
        if x == True:
            c += 1
    return c


preenche_lista(lista)
exibe_lista(lista)
print(conta_elementos(lista))
print(retorna_indice(lista, "oi"))
print(busca(lista, "oi"))