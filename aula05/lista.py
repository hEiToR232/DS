import os
os.system("cls")

#Cria lista vazia
lista = list()
lisa = []

#Criar lista pré-definida
lista = ["string", 80, True]
print(lista)

# append(elemento) - insere um elemento no fnal da lista
lista.append("Novo")
print(lista)

# insert(posicao, elemento) - insere um elemento em alguma posição
lista.insert(2, 1533)
print(lista)

# pop([posicao]) - remove um elemento
os.system("cls")
print(lista)
lista.pop()
print(lista)
lista.pop(2)
print(lista)

# remove(elemento) - remove pelo elemento
os.system("cls")
print("Antes: ",lista)
lista.remove(80)
print("Depois: ",lista)

# index(elemento) - retorna o indice do elemento passado por parametro
lista = ["Edson", 85, True]
os.system("cls")
ind = lista.index(85)
print("Indice: ", ind)

# count(elemento) conta a incedência de elementos na lista
lista = ["Edson", 85, True, 85]
os.system("cls")
qtd = lista.count(85)
print("Quantidade: ", qtd)

# FUNÇÂO len(lista) - Conta a quantidade de elementos da lista
lista = ["Edson", 85, True, 85]
os.system("cls")
qtd = len(lista)
print("Quantidade: ", qtd)

# sum(lista) - Soma os elementos da lista
lista = [12, 22, 65, 88]
os.system("cls")
soma = sum(lista)
print("Quantidade: ", soma)

# concatenacao +
lista1 = [12, 22, 65, 88]
lista2 = [33, 23]
lista3 = lista1 + lista2
print(lista1)
print(lista2)
print(lista3)

# extended(lista) - adiciona uma lista na final da outra
os.system("cls")
lista1 = [12, 22, 65, 88]
lista2 = [33, 23]
print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)
print(lista2)

# copy() - efetua a copia de uma lista
