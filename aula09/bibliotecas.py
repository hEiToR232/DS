"""
DEFINICAO: Verifica se uma string é float
PARÂMETOS:
    v = string
RETORNO: 
    Booleano
"""
def isfloat(v: str) -> bool:
    if v[0] == "-" or v[0] == "+":
        v = v.replace("-", "", 1)
        v = v.replace("+", "", 1)
    v = v.replace(".", "", 1)
    return v.isdigit()
"""
DEFINICAO: Verifica se uma string é int
PARÂMETOS:
    v = string
RETORNO: 
    Booleano
"""
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

def saudacao(usuario:str, hora: int = 8) -> None:
    turno = "Bom dia"
    if(hora > 12):
        turno = "Boa Tarde"
    if(hora > 18):
        turno = "Boa Noite"
    print(f"{usuario}, {turno}! \nSeja ben-vindo!")

# Parametros *args
def soma_numeros(*args) -> float:
    soma = 0
    for num in args:
        soma += num
    return soma
print(soma_numeros(2,3,2,2,3,4,5,3,5,5,3,3,5,5,5,5,5,5,))

"""
1. Verificar se a placa (antiga ou nova) de um carro é válida, retornando True ou False
Quantos parametros? 1 - str
Tipo Retorno? bool
    Antiga: LLL9999
    Nova:   LLL9L99
Exemplos:
453365 - False
rrrr555 - False
ede5555 - True
fly5k44 - True
dir4l99 - True
"""

def placaValida(placa: str) -> bool:
    digito = "0123456789"
    valido = True
    for i in range(0,3):
        if placa[i] in digito:
            valido = False
    if placa[3] not in digito:
        valido = False
    if placa[5] not in digito:
        valido = False
    if placa[6] not in digito:
        valido = False
    return valido
print(placaValida("4533635"))
print(placaValida("rrrr555"))
print(placaValida("ede5555"))
print(placaValida("fly5k44"))
print(placaValida("dir4l99"))
