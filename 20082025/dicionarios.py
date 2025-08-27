dicionario = dict()
dicionario = {}
print(dicionario)

import os
os.system("cls")

aluno = {
    "nome":"Edson",
    "idade": 51,
    "curso": "DS",
}
print(aluno)
print(aluno.get("nota"))
print(aluno.get("idade"))
print(aluno)
aluno["nota"] = 8.9
print(aluno)
aluno.pop("nome")
print(aluno)
aluno["Nota"] = aluno["nota"] + 0.5
print(aluno)
del aluno["Nota"]
print(aluno)

del aluno
print(aluno)


