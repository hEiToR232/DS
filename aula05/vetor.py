import os
os.system("cls")
#        0   1   2   3   4   5
vetor = [45, 59, 55, 32, 45, 44]
# Exibe o vetor integralmente
print(vetor)

# Exibe as posições pelo índice
for i in range(0, len(vetor), 1):# len() retorna quantos elementos temos no vetor
    print(f"vetor[{i}] = {vetor[i]}")

print()
for elem in vetor:
    print(elem)

print()
for ind, elem in enumerate(vetor):
    print(f"Vetor [{ind}] = {elem}")

os.system("cls")
#Exercicios
#1. Somar os elementos do vetor
soma = 0
for i in range(0, 5, 1):
    vetor [i] = int(input("Digite um numero: "))
    soma += vetor[i]
print(soma)
#2. Calcular a media
media = soma / 5
print(media)
#3. Verificar qaundos elementos sao acima da media
am = 0
for i in range(0, 5, 1):
    if vetor[i] > media:
        am += 1
print(am)  

