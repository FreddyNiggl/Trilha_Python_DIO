from funcoes import *


deposito = 0
saque = 0
limite = 500
LIMITE_SAQUES = 3
numero_saques = 0


nome_arquivo = 'extrato_bancario.txt'
if not ler_extrato(nome_arquivo):
    criar_extrato(nome_arquivo)

while True:

    opcao = menu()

    if opcao == 'd':
        valor_depositado = depositando('Que valor deseja depositar ? ')
        registrar(nome_arquivo, valor_depositado)
        

    elif opcao == 's':
        while numero_saques <= LIMITE_SAQUES:
            saldo = saldo_atual(nome_arquivo)
            saques_diarios = sacando('Quanto voce deseja sacar? ', saldo, nome_arquivo, numero_saques)
            numero_saques = saques_diarios
            continuar = str(input('Deseja efetuar outro saque ? [Sim/Nao]')).strip().upper()[0]
            if continuar == 'N':
                break
            if numero_saques == 3:
                print('\033[0;31mSaques indisponiveis por hoje. Tente novamente amanha. Até logo...\033[m') 
                time.sleep(2)
                break

        
    elif opcao == 'z':
        saldo = saldo_atual(nome_arquivo)
        print(f'\033[7mSeu saldo atual é de R$ {saldo}.00\033[m')

    elif opcao == 'e':
        comprovante = "EXTRATO".center(25, '#')
        print(comprovante)
        extrato(nome_arquivo)
        print(comprovante)
        

    elif opcao == 'q':

        numero_saques = 0
        print('\033[7mObrigado por usar nosso sistema bancário. Até a próxima...\033[m')
        break

    else:
        print('Opcao nao encontrada. Tente novamente.')

