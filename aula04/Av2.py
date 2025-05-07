#Enzo Catarino e Heitor Sousa

import os
import random
import time
os.system("cls")
n = 0
resultado = 0
tentativa = 0
acerto1 = 0
acerto2 = 0
acerto3 = 0
erro = 0
pAcerto1 = 0
pAcerto2 = 0
pAcerto3 = 0
pErro = 0
while True:
    num = 0
    print("----------------------------\nMENU\n0 - SAIR\n1 - Sortear o numero\n2 - Jogar\n3 - Estatísticas\n----------------------------")
    n = int(input("Escolha: "))
    os.system("cls")
    if n == 0:
        input("Pressione para sair")
        break
    if n == 1:
        resultado = random.randint(0,10)
        print("Numero sorteado!")
        time.sleep(2)
        os.system("cls")
    if n == 2:
        for cont in range(0, 3, 1):
            if cont == 0:
                num = int(input("PALPITE: "))
                if num == resultado:
                    print("Acertou!")
                    tentativa += 1
                    acerto1 += 1
                    break
                elif num>resultado:
                    print(f"Errou! O numero sorteado está abaixo de {num}")
                    tentativa += 1
                    erro += 1
                elif num<resultado:
                    print(f"Errou! O numero sorteado está acima de {num}")
                    tentativa += 1
                    erro += 1
            if cont == 1:
                num = int(input("PALPITE: "))
                if num == resultado:
                    print("Acertou!")
                    tentativa += 1
                    acerto2 += 1
                    break
                elif num>resultado:
                    print(f"Errou! O numero sorteado está abaixo de {num}")
                    tentativa += 1
                    erro += 1
                elif num<resultado:
                    print(f"Errou! O numero sorteado está acima de {num}")
                    tentativa += 1
                    erro += 1
            if cont == 2:
                num = int(input("PALPITE: "))
                if num == resultado:
                    print("Acertou!")
                    tentativa += 1
                    acerto3 += 1
                    break
                elif num>resultado:
                    print(f"Errou! O numero sorteado está abaixo de {num}")
                    tentativa += 1
                    erro += 1
                elif num<resultado:
                    print(f"Errou! O numero sorteado está acima de {num}")
                    tentativa += 1
                    erro += 1
        print("Fim de jogo!")
        input("Pressione para continuar")
        os.system("cls")
    if n == 3:
        if tentativa > 0:
            pAcerto1 = acerto1*100/tentativa
            pAcerto2 = acerto2*100/tentativa
            pAcerto3 = acerto3*100/tentativa
            pErro = erro*100/tentativa
        print("""
------------------------------------------------
Acertos na primeira tentativa....:{a1:3} -{pa1:6}%
Acertos na segunda tentativa.....:{a2:3} -{pa2:6}%
Acertos na terceira tentativa....:{a3:3} -{pa3:6}%
Não acerto.......................:{e:3} -{pe:6}%                    
        
TOTAL DE TENTATIVAS:{t:4} 
------------------------------------------------    
        """.format(a1=acerto1,a2=acerto2,a3=acerto3,e=erro,t=tentativa,pa1=pAcerto1,pa2=pAcerto2,pa3=pAcerto3,pe=pErro))
        input("PRESSIONE ALGUMA TECLA PARA CONTINUAR...")
        os.system("cls")
