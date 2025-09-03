# Enzo Catarino
# Heitor Sousa
import os
os.system("cls")
lista = list()
dicionario = dict()

def listar_dicionario() -> None:
    print("ESTRUTURA: ")
    print("---------")
    for k, v in dicionario.items():
        print(f"Campo -> {k}       : Tipo -> {type(dicionario[k])}")
    print()

def criando_dicionario() -> None:
    while True:
        print("CRIANDO O DICIONARIO")
        print("--------------------")
        print()
        print("Ponto (.) para finalizar...")
        campo = input("Campo: ")
        if campo == ".":
            break
        else:
            dicionario[campo] = None
            while True:
                print("Tipo: ")
                print("1 -> str")
                print("2 -> int()")
                print("3 -> float()")
                tipo = input("Escolha: ")
                match tipo:
                    case "1":
                        dicionario[campo] = str()
                        break
                    case "2":
                        dicionario[campo] = int()
                        break
                    case "3":
                        dicionario[campo] = float()
                        break
                    case _:
                        print("Tipo inexistente!")
            listar_dicionario()

def cadastrar_registro() -> list:
    lista = list()
    print("PREENCHENDO OS REGISTROS:")
    print("------------------------")
    for k,v in dicionario.items():
        tipo = type(k).__name__
        entrada = input(f"{tipo}  | {k} -> ")
        if tipo == "str":
            entrada = str(entrada)
        elif tipo == "int":
            entrada = int(entrada)
        elif tipo == "float":
            entrada = float(entrada)
        dicionario[k] = entrada
    print("\nRegistro inserido com sucesso!")   
    lista.append(dicionario.copy())

while True:
    print("MENU PRINCIPAL")
    print("--------------")
    print("1 - Criar estrutura do dicionário")
    print("2 - Listar estrutura do dicionário")
    print("3 - Cadastrar registros")
    print("4 - Exibir registros")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        criando_dicionario()
    elif escolha == "2":
        listar_dicionario()
        input()
    elif escolha == "3":
        lista = cadastrar_registro()