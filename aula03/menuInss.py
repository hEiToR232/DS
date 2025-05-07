import os
os.system("cls")
n = 1
while n != 0:
    print("0 - SAIR \n1 - CALCULAR INSS \n2 - CALCULAR IR\n3 - CALCULAR INSS E IR \n4 - CALCULAR O DIGITO DO CPF")
    n = float(input("NUMERO (OU 0 PARA SAIR):"))
    if n == 1 or n == 2 or n == 3:
        valor = int(input("DIGITE O SEU SALARIO: "))
        if n ==1 or n==3:
            if valor <= 1518:
                inss = valor * 0.075
            elif valor > 1518 and valor <= 2793.88:
                inss = valor * 0.09
            elif valor > 2793.88 and valor <= 4190.83:
                inss = valor * 0.12
            elif valor > 4190.83 and valor <= 8157.41:
                inss = valor * 0.14
            elif valor > 8157.41:
                inss = 951.62
        print(f"INSS: R${inss}")   
        
        if n == 2 or n == 3: 
            if valor <= 2259.20:
                ir = 0
            elif valor > 2259.20 and valor <= 2826.65:
                ir = valor * 0.075
            elif valor > 2826.65 and valor <= 3751.05:
                ir = valor * 0.15
            elif valor > 3751.05 and valor <= 4664.68:
                ir = valor * 0.225
            elif valor > 4664.68: 
                ir = valor * 0.275
            print(f"IR: R${ir}") 
     
    elif n == 4:
        dig1 = int(input("DIGITE O 1º DÍGITO DO CPF: "))
        dig2 = int(input("DIGITE O 2º DÍGITO DO CPF: "))
        dig3 = int(input("DIGITE O 3º DÍGITO DO CPF: "))
        dig4 = int(input("DIGITE O 4º DÍGITO DO CPF: "))
        dig5 = int(input("DIGITE O 5º DÍGITO DO CPF: "))
        dig6 = int(input("DIGITE O 6º DÍGITO DO CPF: "))
        dig7 = int(input("DIGITE O 7º DÍGITO DO CPF: "))
        dig8 = int(input("DIGITE O 8º DÍGITO DO CPF: "))
        dig9 = int(input("DIGITE O 9º DÍGITO DO CPF: "))

        soma = (dig1 * 10) + (dig2 * 9) + (dig3 * 8) + (dig4 * 7) + (dig5 * 6) + (dig6 * 5) + (dig7 * 4) + (dig8 * 3) + (dig9 * 2)
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto
        
        soma = (dig1 * 11) + (dig2* 10) + (dig3 * 9) + (dig4 * 8) + (dig5 * 7) + (dig6 * 6) + (dig7 * 5) + (dig8 * 4) + (dig9 * 3) + (digito1 * 2)
        resto = soma %11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto 
        print(f"OS DIGITOS DO SEU CPF SÃO: {digito1}{digito2}")    
    input("\nPRESSIONE ALGUMA TECLA PARA CONTINUAR...")
    os.system("cls")