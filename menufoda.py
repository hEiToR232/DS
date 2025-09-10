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
        print(f"Campo -> {k:20}: Tipo -> {type(dicionario[k])}")
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

def isfloat(v: str) -> bool:
    if v[0] == "-" or v[0] == "+":
        v = v.replace("-", "", 1)
        v = v.replace("+", "", 1)
    v = v.replace(".", "", 1)
    return v.isdigit()

def isint(v:str) -> bool:
    digito = "0123456789"
    valido = True
    if v[0] in "+-" or v[0] in digito:
        for i in range(1, len(v)):
            if v[i] not in digito:
                valido = False
                break
    else:
        valido = False
    return valido

def cadastrar_registro() -> dict:
    print("PREENCHENDO OS REGISTROS:")
    print("------------------------")
    for k,v in dicionario.items():
        tipo = type(v).__name__
        entrada = input(f"{tipo:10}| {k} -> ")
        if tipo == "str":
            while isfloat(entrada) or isint(entrada):
                print("Valor invalido para str! ")
                entrada = input(f"{tipo}  | {k} -> ")
        elif tipo == "int":
            while not isint(entrada):
                print("Valor invalido para int! ")
                entrada = input(f"{tipo}  | {k} -> ")
            entrada = int(entrada)
        elif tipo == "float":
            while not isfloat(entrada):
                print("Valor invalido para float! ")
                entrada = input(f"{tipo}  | {k} -> ")
            entrada = float(entrada)
        dicionario[k] = entrada
    print("\nRegistro inserido com sucesso!")   
    return dicionario.copy()


def exibe_tabela(tab: list) -> None:
    print("EXIBINDO A TABELA:")
    print("-------------------")
    for idx, reg in enumerate(tab, start=1):
        print(f"Registro {idx}")
        for k, v in reg.items():
            print(f"{k:10}........: {v}")
        print()

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
        lista.append(cadastrar_registro())
    elif escolha == "4":
        exibe_tabela(lista)