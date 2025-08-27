import os
os.system("cls")

tabela = list()
registro = dict()


def digita_registro(reg: dict) -> None:
    reg["nome"] = input()
    reg["idade"] = input()
    reg["curso"] = input()

def add_registro(tab: list, reg: dict) -> None:
    tab.append(reg.copy())


digita_registro(registro)
add_registro(tabela, registro)



registro["nome"] = "Marion"
registro["idade"] = 56
registro["curso"] = "adm"

tabela.append(registro.copy())

"""
print(tabela[0]["nome"],tabela[0]["idade"],tabela[0]["curso"])
print(tabela[1]["nome"],tabela[1]["idade"],tabela[1]["curso"])
print()

for i in range(len(tabela)):
    print(tabela[i]["nome"],tabela[i]["idade"],tabela[i]["curso"])

print()

for reg in tabela:
    print(reg["nome"],reg["idade"],reg["curso"])

    print()
"""
def exibe_tabela(tab: list)-> None:
    for reg in tabela:
        for k, v in reg.items():
            print(f"{k} : {v} --> {type(v)}")
        print()

exibe_tabela(tabela)