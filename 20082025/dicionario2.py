import os
os.system("cls")

aluno = {
    "nome_do_pai":"Edson",
    "idade": 51,
    "curso": "DS",
}
# métodos
print(aluno)
# keys() - cria uma LISTA com as chaves
print(aluno.keys())
# values() - cria uma lista com as values
print(aluno.values())
# items() - cria uma lista com os itens do dicionario
print(aluno.items())

# campos
print()
for k in aluno.keys():
    print(k.capitalize())
print(aluno.keys())

# valores
print()
for v in aluno.values():
    print(v)
print(aluno.keys())

# items
print()
for k, v in aluno.items():
    print(f"Campo: {k:15} --> Valor: {v}")
print(aluno.items())

aluno["nome"] = "rua tal"