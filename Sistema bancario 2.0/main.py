import textwrap
from funcoes import *

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("\033[7mInforme o valor do depósito: \033[m"))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            valor = float(input("\033[7mInforme o valor do saque: \033[m"))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato, 
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\033[0;31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")

main()