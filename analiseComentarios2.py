# Enzo Catarino
# Heitor Sousa
import os
os.system('cls')

lista_comentario = [
    "O produto é excelente e muito bom!",
    "Péssimo atendimento. Horrível!",
    "A entrega foi ruim, mas o produto é bom",
    "Ótimo custo-benefício",
    "Não gostei, é horrível"
]

def exibe_comentario(lista_c: list) -> None:
    for i, comentario in enumerate(lista_comentario, start=1):
        print(f"{i}. {comentario}")

def adiciona_comentario() -> None:
    novo = input("Inclua um novo comentario: ")
    lista_comentario.append(novo)

positiva = ['bom', 'otimo', 'excelente']
negativa = ['ruim', 'horrivel', 'pessimo']
vazias = ["o", "a", "as", "os", "de", "e", "mas"]

def tirar_acento(msg: str) -> str:
    cAcento = "áàãâéèêíìîïóòõôúùûç"
    sAcento = "aaaaeeeiiiioooouuuc"
    retorno = ""
    for letra in msg:
        if letra in cAcento:
            idc = cAcento.index(letra)
            retorno += sAcento[idc]
        else:
            retorno += letra
    return retorno

def analisar_comentario(list_c: list) -> None:
    conta_positivo = 0
    conta_negativo = 0
    palavras_uteis = 0
    
    for i, comentario in enumerate(list_c):
        c = str(comentario.lower())
        c = tirar_acento(c)
        texto = c.replace("!", "").replace(".", "").split()

        texto_filtrado = []
        for palavra in texto:
            if palavra not in vazias:
                texto_filtrado.append(palavra)

        palavras_uteis += len(texto_filtrado)

        tem_positivo = False
        tem_negativo = False
        
        for palavra in texto_filtrado:
            if palavra in positiva:
                tem_positivo = True
            if palavra in negativa:
                tem_negativo = True

        print(f"\n--- Comentário {i+1}: '{comentario}' ---")
        print(f"Palavras filtradas: {texto_filtrado}")
        print(f"Contém palavra positiva? {tem_positivo}")
        print(f"Contém palavra negativa? {tem_negativo}")

        if tem_positivo:
            conta_positivo += 1
        if tem_negativo:
            conta_negativo += 1

    print("\n===== RESULTADO DA ANÁLISE =====")
    print(f"Comentários positivos: {conta_positivo}")
    print(f"Comentários negativos: {conta_negativo}")
    print(f"Total de palavras úteis analisadas: {palavras_uteis}")

while True:
    print('''
MENU--------------------------------------------------------------------------------

1. Exibir comentarios
2. Adicionar comentarios
3. Analisar comentarios
4. Sair

------------------------------------------------------------------------------------
''')
    escolha = input('Escolha: ')
    os.system('cls')

    if escolha == '1':
        print('Comentarios:')
        print()
        exibe_comentario(lista_comentario)
        input()
        os.system('cls')

    elif escolha == '2':
        adiciona_comentario()
        os.system('cls')

    elif escolha == '3':
        analisar_comentario(lista_comentario)
        input()
        os.system('cls')
    
    elif escolha == '4':
        break