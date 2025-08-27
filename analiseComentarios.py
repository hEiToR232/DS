# Enzo Catarino
# Heitor Sousa

def maior_valor(l: list) -> int:
    maior = l[0]
    for i in range (1,len(l)):
        if l[i] > maior:
            maior = l[i]
    return maior
lista = [20,0,5,3]
print(maior_valor(lista))

def conta_vogais(msg: str) -> int:
    vogais = "AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ"
    qtd = 0
    for letra in msg:
        if letra.upper() in vogais:
            qtd+=1
    return qtd
entrada = "Python é divertido"
print(conta_vogais(entrada))

def palavras_maiores(msg: str, n: int) -> list:
    lista_mensagem = msg.split()
    lista_retorno = list()
    for palavra in lista_mensagem:
        if len(palavra) > n:
            lista_retorno.append(palavra)
    return lista_retorno
entrada = "Hoje é um excelente dia para estudar Python"
n1 = 5
print(palavras_maiores(entrada, n1))

def conta_pares(nums: str) -> int:
    lista_numeros = nums.split()
    qtd = 0
    for num in lista_numeros:
        if int(num) % 2 == 0:
            qtd+=1
    return qtd
entrada = "4 7 2 9 10 13"
print(conta_pares(entrada))

def formata_texto(texto: list) -> str:
    return " ".join(texto)
entrada = ["Programar","em","Python","é","divertido"]
print(formata_texto(entrada))

import os
os.system("cls")

# Enzo Catarino
# Heitor Sousa
import os
os.system('cls')

lista_comentario = [
"O produto é excelente e muito bom!",
"Péssimo atendimento. Horrível!",
"A entrega foi ruim, mas o produto é bom",
"Ótimo custo-benefício",
"Não gostei, é horrível"
]

def exibe_comentario(lista_c: list):
    for comentario in enumerate(lista_comentario, start=1):
        print(comentario)

def adiciona_comentario():
    novo = input("Inclua um novo comentario: ")
    lista_comentario.append(novo)

positiva = ['bom', 'ótimo', 'excelente']
negativa = ['ruim', 'horrivel', 'péssimo']

def analisar_comentario(list_c: list):
    conta_positivo = 0
    conta_negativo = 0
    palavra_util = 0
    for comentario in list_c:
        c = comentario.lower()
        texto = c.split()
        if any(palavra in texto for palavra in positiva):
            conta_positivo += 1
        elif any(palavra in texto for palavra in negativa):
            conta_negativo += 1
    palavra_util = conta_negativo + conta_positivo
    print(f'Comentarios positivos {conta_positivo}')
    print(f'Comentarios negativos {conta_negativo}')
    print(f'Palavras uteis {palavra_util}')

while True:
    print('''
MENU--------------------------------------------------------------------------------

1. Exibir comentarios
2. Adicionar comentarios
3. Analisar comentarios
4. Sair
      
------------------------------------------------------------------------------------
''')
    escolha = input('Escolha: ')

    os.system('cls')

    if escolha == '1':
        print('Comentarios:')
        print()
        exibe_comentario(lista_comentario)
        input()
    os.system('cls')

    if escolha == '2':
        adiciona_comentario()
    os.system('cls')

    if escolha == '3':
        print('RESULTADO DA ANALISE')
        print()
        analisar_comentario(lista_comentario)
        input()
    os.system('cls')
    
    if escolha == '4':
        break