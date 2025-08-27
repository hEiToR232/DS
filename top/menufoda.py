# Enzo Catarino
# Heitor Sousa
import os
os.system("cls")

lista = list()
dicionario = dict()
while True:
    print("MENU PRINCIPAL")
    print("--------------")
    print("1 - Criar estrutura do dicionário")
    print("2 - Listar estrutura do cidionário")
    print("3 - Cadastrar registros")
    print("4 - Exibir registros")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("CRIANDO O DICIONARIO")
        print("--------------------")
        print()
        print("Ponto (.) para finalizar...")
        campo = input("Campo: ")
        dicionario[campo] = None
        print("Tipo: ")
        print("1 -> str")
        print("2 -> int()")
        print("3 -> float()")
        tipo = input("Escolha: ")
        if tipo == "1":
            dicionario[campo] = "str"
        if tipo == "2":
            dicionario[campo] = int()
        if tipo == "3":
            dicionario[campo] = "float"
        print("ESTRUTURA:")
        print("---------")
        print(f"Campo -> {campo}      : Tipo ->  {type(dicionario[campo])}")            
        input()


            
            
        