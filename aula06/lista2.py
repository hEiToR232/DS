import os
os.system("cls")

# copy() - efetua a copia de uma lista

lista1 = [1,2,3]
lista2 = lista1.copy()
print(lista1)
print(lista2)
lista1[0] = 99
print(lista1)
print(lista2)

# Método sort()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)

lista.sort()
print(lista)

# Parametro Reverse - organiza em ordem decrescente
lista.sort(reverse = True)
print(lista)

# Método reverse()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
lista.reverse()
print(lista)

# Método clear()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
lista.clear()
print(lista)

# Comando del()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
del lista
print(lista)



'''
lista1 =[1,2,3]
lista2 = lista1
print(lista1)
print(lista2)
lista1[0] = 99
print(lista1)
print(lista2)
'''
