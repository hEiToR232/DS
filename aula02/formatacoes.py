import os
os.system("cls")

nome = "Edson de Oliveira"
idade = 50
salario = 45987.85

# Forma 1 - clássica (separa dados de quaisquer tipo)
print(nome, idade, salario)
print("nome: ", nome, "\nidade: ", idade, "\nsalario: ", salario)

#Forma 2 - Utilizando a função format
#                                                   0     1      2
print("Nome: {0}\nIdade: {1}\nSalario: {2}".format(nome,idade,salario))
print("Nome: {n}\nIdade: {i:05d}\nSalario: {s:14.2f}".format(n=nome,i=idade,s=salario))

# Forma 3 - utilizando o fprint

print(f"Nome: {nome}\nIdade: {idade}\nSalario: {salario}")
print(f"Nome: {nome}\nIdade: {idade}\nSalario: {salario}")

# Forma 4 - Utilizando triple quotes 
print(f"Nome: {nome}", end = ".")
print(f"Idade: {idade}", end = ".")
print(f"Salario: {salario}", end = ".")

print(f"""
      Nome: {nome}
      Idade: {idade}
      Salario: {salario}
      """)
