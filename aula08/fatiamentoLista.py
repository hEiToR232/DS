import os
os.system("cls")

# Fatiamento
#         0   1   2   3    4   5   6   7   8   9
numero = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#        -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(numero)
print(numero[6])
print(numero[-3])
n = numero[3:7]
print(n)
print(numero[2:9:3])
print(numero[9:2:-2])
print(numero[-3:])
print(numero[::-1])

# Tupla
lista = [1, 2, 3, 4, 5] # list()
tupla = (1, 2, 3, 4, 5) # tuple()
print(tupla[3])
print(type(lista), type(tupla))
x = list(tupla)
print(type(x))

# Fatiamento de String

frase = "Subi no Onibus"
print(frase)
print(frase[2])
print(frase[2:10])
print(frase[::3])
print(frase[::-1])

# metodos para string
#        012345678901234567890123456789012345678901234567890
frase = "Agora veremos como funciona o fatiamento de strings"

#find(substrinc, inicio,fim) -> busca uma substring
print(frase.find("como"))
print(frase.find("x")) # -1 nao existe
print(frase.find("a"))
print(frase.find("a", 10, 30))

# Exercicios 1
os.system("cls")

def procura_substr(texto:str, sub_texto:str, inicio:int ,fim:int):
    ind = list()
    while True:
        indice = texto.find(sub_texto, inicio, fim + 1)
        if indice == -1:
            break
        else:
            ind.append(indice)
            inicio = indice + 1
    return ind    
frase = "Testando a funcao"
indice = procura_substr(frase, "a", 0, 16)
if not indice:
    print("Não existe esse caractere!")
else:
    print(indice)

os.system("cls")
# join(lista_de_strings) -> junte uma lista de strings em uma string
lista_nome = ["Edson", "de", "Oliveira"]
print(lista_nome)
str_nome = " ".join(lista_nome)
print(str_nome)

# split(str_separadora) -> contrário de join
os.system("cls")
nome = "Edson de Oliveira"
print(nome)
print(nome.split())

# replace(procura, troca, cont)
os.system("cls")
nome = "Edson de Oliveira"
print(nome.replace("e", "E"))
print(nome.replace("de", "minha nossa nossa nossa"))
print(nome.replace("e", "E", 2))

#strip() -> elimnina os espaços das extremidades
os.system("cls")
texto = "          elimina os espaços    "
print(texto)
print(texto.strip())

#operador in
os.system("cls")
x = "E"
if x in "Edson":
    print(f"tem {x}")
else:
    print(f"não tem {x}")
numeros = [42, 23, 21, 12, 23]
if 42 in numeros:
    print(f"esta")
else:
    print(f"nao esta")


# 1. crie a função: vogal_maiuscula(string) -> str:
os.system("cls")
def vogal_maiuscula(texto: str) -> str:
    texto = texto.replace("a", "A")
    texto = texto.replace("e", "E")
    texto = texto.replace("i", "I")
    texto = texto.replace("o", "O")
    texto = texto.replace("u", "U")
    return texto
txt = "aeiou bom dia andrade viado"
upper = vogal_maiuscula(txt)
print(upper)
'''
2. cria a função: isfloat(string) -> boolean:
    resp = isfloat("edson") # False
    resp = isfloat("45.78") # True
    resp = isfloat("65") # True
    resp = isfloat("-98") # True
    resp = isfloat("234,67") # False
    resp = isfloat("+22.78") # True
    resp = isfloat("44.777.88") # False
'''
def isfloat(r) -> bool:
    try:
        float(r)
        return True
    except ValueError:
        return False
print(isfloat("edson"))# False
print(isfloat("45.78")) # True
print(isfloat("65")) # True
print(isfloat("-98")) # True
print(isfloat("234,67")) # False
print(isfloat("+22.78")) # True
print(isfloat("44.777.88")) # False

        

