"""
EXERCICIOS:
crie um dicionário (com 3 campos preenchidos) e um menu, como 
a sugestão abaixo, para manipular o dicionário.
1 - Acrescentar campo
2 - Remover campo
3 - Editar o registro
        (a) Nome
        (b) Idade
        (c) Nota
4 - Mostrar o registro
0 - SAIR

"""

import os 

d = {
    "nome":"ronaldo",
    "idade":69,
    "nota":7.2,
}

def adicionar_campo() -> None:
    campo = input("Adicione um campo:")
    valor = input("Adicione um valor ao seu campo: ")
    d[campo] = valor
    print(f"Campo {campo} adicionado com sucesso")

def remover_campo() -> None:
    campo = input("Remova um campo: ")
    if campo in d:
        del d[campo]
        print(f"Campo {campo} removido com sucesso")
    else:
        print("Campo não encontrado")

def editar_registro() -> None:
    print("O que deseja editar?")
    print("(a) Nome")
    print("(b) Idade")
    print("(c) Nota") 
    opcao = input("Escolha: ")
    opcao.lower()

    if opcao == "a":
        d["nome"] = input("Novo nome: ")
    elif opcao == "b":
        d["idade"] = input("Nova idade: ")
    elif opcao == "c":
        d["nota"]
    else:
        print("Opcao invalida")
    print("Registro atualizado")

def mostrar_registro() -> None:
    print("Registro atual: ")
    for k, v in d.items():
        print(f"{k}: {v}")
    print()

while True:
    print("===MENU===")
    print("1 - Acrescentar campo")
    print("2 - Remover campo")
    print("3 - Editar o registro")
    print("4 - Mostrar registro")
    print("0 - Sair")
    escolha = int(input("Digite sua escolha: "))

    os.system("cls")

    if escolha == 1:
        adicionar_campo()
    elif escolha == 2:
        remover_campo()
    elif escolha == 3:
        editar_registro()
    elif escolha == 4:
        mostrar_registro()


    
