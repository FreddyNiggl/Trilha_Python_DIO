import textwrap

def menu():
    menu = """\n
    ============== MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNovo Conta
    [6]\tListar Conta
    [0]\tSair
    => """
    # return input(menu)
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0: 
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n\033[0;32mDeposito realizado com sucesso!\033[m")
    else: 
        print("\n\033[0;31mOperação falhou! O valor informado é invalido.\033[m")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n\033[0;31mOperacao Falhou! Voce nao tem saldo suficiente.\033[m")
    elif excedeu_limite:
        print('\033[0;31mOperaao Falhou! O valor do saque excede o limite.\033[m')
    elif excedeu_saques:
        print("\n\033[0;31mOperacao Falhou! Numero maximo de saques excedido.\033[m")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n\033[0;32mSaque Realizado com Sucesso!\033[m")
    else:
        print(f"\033[0;31mOperacao Falhou! Valor informado é Invalido.\033[m")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO==========")
    print("\033[7mNão foram realizados movimentações.\033[m" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n==========EXTRATO==========")
    
def criar_usuario(usuarios):
    cpf = input("\033[7mInforme o CPF (somente numeros)\033[m")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[0;31mOperacao Falhou! Já existe usuário com esse CPF.\033[m")
        return 
    
    nome = input("\033[7mInforme o nome Completo: \033[m")
    data_nascimento = input("\033[7mInforme a data de nascimento (dd-mm-aaaa): \033[m")
    endereco = input("\033[7mInforme o endereço (logradouro, nro - bairro - cidade/sigla estado): \033[m")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\033[0;32mUsuario criado com sucesso!\033[m")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\033[7mInforme o CPF do usuario: \033[m")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[0;32mConta criada com sucesso!\033[m")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}   
    
    print("\n\033[0;31mUsuário nao encontrado, fluxo de criação de conta encerrado!\033[m")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
