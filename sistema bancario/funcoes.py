import time


def menu():
    opcao = str(input(""" 
[d] Deposito
[s] Saque
[z] Saldo
[e] Extrato
[q] Sair

Sua escolha -> 
"""))

    return opcao



def depositando(txt):
    while True:
        valor = str(input(txt)).strip()
        if valor.isnumeric():
            valor = int(valor)
            return valor

        elif valor.isalpha() or valor == '':
            print('Por favor, insiro um valor válido')

        else:
            print('Valor por favor digite um numero válido')



def ler_extrato(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo nao encontrado')
        return False
    else:
        print('Arquivo lido com sucesso')
        return True



def criar_extrato(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('Problema na criacao do arquivo')
    else:
        print('Arquivo criado com sucesso!')



def registrar(arquivo, valor_depositado=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Problema para abrir o arquivo')
    else:
        try:
            arq.write(f'Valor depositado: R$ + {valor_depositado:.2f}\n')
        except:
            print('\033[;31Problema para escrever no extrato\033[md]')
        else:
            print('\033[;32mValor registrado com sucesso\033[m')



def valor_positivo(arq):
    try:
        extrato = open(arq, 'rt')
    except:
        print('Nao consegui ler o arquivo')
    else:
        total_pos = 0
        for linha in extrato:
            if '+' in linha:
                conteudo_linha = linha.split('+')
                valor = conteudo_linha[1].strip().split('.')
                valor[0] = int(valor[0]) if valor[0].isnumeric() else print('Valor inválido')
                total_pos += valor[0]
        return total_pos
        

def valor_negativo(arq):
    try:
        extrato = open(arq, 'rt')
    except:
        print('Nao consegui ler o arquivo')
    else:
        total_neg = 0
        for linha in extrato:
            if '-' in linha:
                conteudo_linha = linha.split('-')
                valor = conteudo_linha[1].strip().split('.')
                valor[0] = int(valor[0]) if valor[0].isnumeric() else print('Valor inválido')
                total_neg += valor[0]
        return total_neg
     
        
def saldo_atual(arq):
    pos = valor_positivo(arq) 
    neg = valor_negativo(arq)
    soma = pos - neg
    return soma


def sacando(txt, total_disponivel, arq, quant_saques):
    while True:
        valor_saque = str(input(txt)).strip()
        if valor_saque.isnumeric():
            valor_saque = int(valor_saque)
            break
        elif valor_saque == '' or valor_saque.isalpha:
            print('Por favor insira um valor válido!')
        
    if  500 >= valor_saque <= total_disponivel:
        quant_saques = qt_saques(quant_saques)
        print(f"Este é seu {quant_saques}° saque de hoje. Seu limite é de 3 saques ao dia.")
        print('\033[;32mPor favor aguarde enquanto a operação é finalizada. Efetuando saque...\033[m')
        time.sleep(2)
        
        arquivo = open(arq, 'at')
        arquivo.write(f'Valor sacado: R$ - {valor_saque}.00\n')
        arquivo.close()
        arquivo = open(arq, 'at')
        time.sleep(1)
        saldo = saldo_atual(arq)
        print(f'Seu saldo atual é de R${saldo}.00')
        return quant_saques
        
    
    elif valor_saque > 500:
        print('\033[0;31mSeu saque limite é de 500 reais. Por favor tente novament sando um valor menor.\033[m')
        return quant_saques

        
    elif valor_saque > total_disponivel:
        print('\033[0;31mSaldo insuficiente. Por favor, confira seu saldo e tente novamente.\033[m')
        return quant_saques

def extrato(arq):
    try:
        extrato = open(arq, 'rt')
    except:
        print('Nao consegui ler o arquivo')
    else:
        # print('Leitura realizada')
        for linha in extrato:
            print(f"\033[7m{linha}\033[m")
        saldo = saldo_atual(arq)
        print(f'\033[7;32mSeu saldo atual é de R${saldo}.00\033[m')
            
        

def qt_saques(qt):
    qt += 1
    return qt
    