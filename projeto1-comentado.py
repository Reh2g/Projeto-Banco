from datetime import datetime, timedelta
import os

def criarConta():                                                                                                                                                   # ★ Criar conta:
    nome = input('Digite seu nome: ')                                                                                                        # Input de informações para criar conta.
    cpfReal = int(input('Digite seu CPF: '))
    cpf = str(cpfReal)
    senhaReal = int(input('Digite uma senha (apenas números): '))
    senha = str(senhaReal)
    valor = float(input('Digite o valor inicial da conta: '))
    print('\n1 = Salário: \n● Cobra taxa de 5% a cada débito realizado;\n● Não permite débitos que deixem a conta com saldo negativo.')         # Mostra as opções de tipos de conta.
    print('\n2 = Comum \n● Cobra taxa de 3% a cada débito realizado;\n● Permite um saldo negativo de até (R$ 500,00).')
    print('\n3 = Plus \n● Cobra taxa de 1% a cada débito realizado;\n● Permite um saldo negativo de até (R$ 5.000,00).')
    tipo = input('\nEscolha um dos tipos de conta acima: ')

    if tipo != '1' and tipo != '2' and tipo != '3':                                                                                   # Define erro se entrar com valores diferentes.
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Esse tipo não é uma opção oferecida pelo banco...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    elif os.path.isfile(cpf + '(0)' + '.txt'):                                                                                         # Define erro se entrar com CPF já registrado.
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Esse CPF já foi registrado...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        arquivo = open(cpf + '(0)' + '.txt', 'w')                                                                                                # Cria nova conta (em arquivo .txt).
        data = datetime.now()
        arquivo.write('%s\n' % nome)        
        arquivo.write('%s\n' % cpf)
        arquivo.write('%s\n' % senha)
        arquivo.write('%.2f\n' % valor)
        arquivo.write('%s\n' % tipo)
        arquivo.write('%.2f\n' % valor)
        arquivo.write('Criar Conta')
        arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S\n'))
        arquivo.write('0.00')
        arquivo.close()
        print('\n★ Conta criada com sucesso!\n')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def apagarConta():                                                                                                                                                 # ★ Apagar conta:
    confirmaCPF = input('Digite seu CPF: ')                                                                                                                              # Input CPF.

    contador = 0                                                                                                   # Contador para verificar o arquivo mais recente, com o Input CPF.
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                             # Verifica se o arquivo mais recente computado existe, com o Input CPF e Contador.
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()                                                                                                   # Salva a senha para utilizar depois nessa def.
        confirmaSenha = dados[2]
        confirmaSenha = confirmaSenha.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')                                                                                                                       # Input senha.

        if senhaInput == confirmaSenha:                                                                                                  # Verifica se a senha input é igual a senha.
            confirmacao = input('Digite sua senha para prosseguir (DELETAR SUA CONTA É UMA AÇÃO IRREVERSÍVEL): ')
            if confirmacao == senhaInput:                                                                                           # Verifica se confirma senha é igual senha input.
                contadorDel = contador
                for contadorDel in range(contadorDel, -1, -1):                              # Contador para deletar a conta (todos os arquivos .txt, do mais recente ao mais antigo).
                    contadorStrDel = str(contadorDel)
                    os.remove(confirmaCPF + '(' + contadorStrDel + ')' + '.txt')
                print('\n★ Conta deletada com sucesso!\n')
                input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')                                                          # Define erro caso CPF e/ou senha estiverem incorretos.
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def debitar():                                                                                                                                                          # ★ Debitar:
    confirmaCPF = input('Digite seu CPF: ')                                                                                                                              # Input CPF.

    contador = 0                                                                                                   # Contador para verificar o arquivo mais recente, com o Input CPF.
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                             # Verifica se o arquivo mais recente computado existe, com o Input CPF e Contador.
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()                                                                                             # Salva a informações para utilizar depois nessa def.
        nome = dados[0]
        confirmaSenha = dados[2]
        valor = dados[3]
        tipo = dados[4]
        nome = nome.rstrip('\n')
        confirmaSenha = confirmaSenha.rstrip('\n')
        valor = valor.rstrip('\n')
        tipo = tipo.rstrip('\n')
        valorInicial = float(valor)
        arquivo.close()
        senhaInput = input('Digite sua senha: ')                                                                                                                      # Input senha.

        if senhaInput == confirmaSenha:                                                                                                 # Verifica se a senha input é igual a senha.
            valorDebitar = float(input('Digite o valor que você deseja retirar: '))                                                                # Input valor que deseja retirar.
            if tipo == '1':                                                                                                                   # Verifica se a conta é tipo: Salário.
                tarifa = (valorDebitar * 5) / 100                                                                                          # Define tarifa da conta do tipo Salário.
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < 0:                                                                                       # Define erro caso a conta Salário fique com saldo negativo.
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 0,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                                                # Contador para criar um novo arquivo .txt.
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')                                                                 # Cria um novo arquivo .txt.
                    data = datetime.now()
                    arquivo.write('%s\n' % nome)        
                    arquivo.write('%s\n' % confirmaCPF)
                    arquivo.write('%s\n' % confirmaSenha)
                    arquivo.write('%.2f\n' % valorNovo)
                    arquivo.write('%s\n' % tipo)
                    arquivo.write('%.2f\n' % valorDebitar)
                    arquivo.write('Debito')
                    arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S\n'))
                    arquivo.write('%.2f\n' % tarifa)
                    arquivo.close()
                    print('\n★ Dinheiro debitado com sucesso!\n')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
            elif tipo == '2':                                                                                                                   # Verifica se a conta é tipo: Comum.
                tarifa = (valorDebitar * 3) / 100                                                                                            # Define tarifa da conta do tipo Comum.
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < -(500):                                                                      # Define erro caso a conta Comum fique com saldo negativo de R$ -500,00.
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 500,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                                               # Contador para criar um novo arquivo .txt.
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')                                                                # Cria um novo arquivo .txt.
                    data = datetime.now()
                    arquivo.write('%s\n' % nome)        
                    arquivo.write('%s\n' % confirmaCPF)
                    arquivo.write('%s\n' % confirmaSenha)
                    arquivo.write('%.2f\n' % valorNovo)
                    arquivo.write('%s\n' % tipo)
                    arquivo.write('%.2f\n' % valorDebitar)
                    arquivo.write('Debito')
                    arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S\n'))
                    arquivo.write('%.2f\n' % tarifa)
                    arquivo.close()
                    print('\n★ Dinheiro debitado com sucesso!\n')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
            elif tipo == '3':                                                                                                                    # Verifica se a conta é tipo: Plus.
                tarifa = (valorDebitar * 1) / 100                                                                                             # Define tarifa da conta do tipo Plus.
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < -(5000):                                                                    # Define erro caso a conta Plus fique com saldo negativo de R$ -5.000,00.
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 5.000,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                                                # Contador para criar um novo arquivo .txt.
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')                                                                 # Cria um novo arquivo .txt.
                    data = datetime.now()
                    arquivo.write('%s\n' % nome)
                    arquivo.write('%s\n' % confirmaCPF)
                    arquivo.write('%s\n' % confirmaSenha)
                    arquivo.write('%.2f\n' % valorNovo)
                    arquivo.write('%s\n' % tipo)
                    arquivo.write('%.2f\n' % valorDebitar)
                    arquivo.write('Debito')
                    arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S\n'))
                    arquivo.write('%.2f\n' % tarifa)
                    arquivo.close()
                    print('\n★ Dinheiro debitado com sucesso!\n')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')                                                         # Define erro caso CPF e/ou senha estiverem incorretos.
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def depositar():                                                                                                                                                       # ★ Debitar:
    confirmaCPF = input('Digite seu CPF: ')                                                                                                                             # Input CPF.

    contador = 0                                                                                                  # Contador para verificar o arquivo mais recente, com o Input CPF.
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                            # Verifica se o arquivo mais recente computado existe, com o Input CPF e Contador.
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()                                                                                            # Salva a informações para utilizar depois nessa def.
        nome = dados[0]
        confirmaSenha = dados[2]
        valor = dados[3]
        tipo = dados[4]
        nome = nome.rstrip('\n')
        confirmaSenha = confirmaSenha.rstrip('\n')
        valor = valor.rstrip('\n')
        tipo = tipo.rstrip('\n')
        valorInicial = float(valor)
        arquivo.close()
        valorDepositar = float(input('Digite a quantia que você deseja depositar: '))                                                              # Input valor que deseja colocar.
        valorNovo = valorInicial + valorDepositar

        contador = 1                                                                                                                     # Contador para criar um novo arquivo .txt.
        contadorStr = str(contador)
        while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
            contador += 1
            contadorStr = str(contador)

        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')                                                                             # Cria um novo arquivo .txt.
        data = datetime.now()
        arquivo.write('%s\n' % nome)
        arquivo.write('%s\n' % confirmaCPF)
        arquivo.write('%s\n' % confirmaSenha)
        arquivo.write('%.2f\n' % valorNovo)
        arquivo.write('%s\n' % tipo)
        arquivo.write('%.2f\n' % valorDepositar)
        arquivo.write('Deposito')
        arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S\n'))
        arquivo.write('0.00')
        arquivo.close()
        print('\n★ Dinheiro depositado com sucesso!\n')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! O CPF está incorreto...')                                                                                           # Define erro caso CPF estiver incorreto.
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def saldo():                                                                                                                                                              # ★ Saldo:
    confirmaCPF = input('Digite seu CPF: ')                                                                                                                              # Input CPF.

    contador = 0                                                                                                   # Contador para verificar o arquivo mais recente, com o Input CPF.
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):                             # Verifica se o arquivo mais recente computado existe, com o Input CPF e Contador.
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()                                                                                             # Salva a informações para utilizar depois nessa def.
        confirmaSenha = dados[2]
        valor = dados[3]
        confirmaSenha = confirmaSenha.rstrip('\n')
        valor = valor.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')                                                                                                                       # Input senha.

        if senhaInput == confirmaSenha:                                                                                                  # Verifica se a senha input é igual a senha.
            print('\n★ Seu saldo atual é de: R$ %s\n' % valor)                                                                         # Mostra o saldo do arquivo .txt mais recente.
            input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
        else:
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')                                                      # Define erro caso CPF e/ou senha estiverem incorretos.
            input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def extrato():                                                                                                                                                          # ★ Extrato:
    confirmaCPF = input('Digite seu CPF: ')                                                                                                                              # Input CPF.

    if os.path.exists(confirmaCPF + '(0)' + '.txt'):                                                                                         # Verifica se a conta existe, com o CPF.
        arquivo = open(confirmaCPF + '(0)' + '.txt', 'r')
        dados = arquivo.readlines()                                                                                             # Salva a informações para utilizar depois nessa def.
        nome = dados[0]
        confirmaSenha = dados[2]
        tipo = dados[4]
        nome = nome.rstrip('\n')
        confirmaSenha = confirmaSenha.rstrip('\n')
        tipo = tipo.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')                                                                                                                       # Input senha.

        if senhaInput == confirmaSenha:                                                                                                  # Verifica se a senha input é igual a senha.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿\n')                                                                                         # Print Nome, CPF e Tipo de conta.
            print('Nome: %s' % nome)
            print('CPF: %s' % confirmaCPF)
            if tipo == '1':
                print('Conta: Salário')
            elif tipo == '2':
                print('Conta: Comum')
            elif tipo == '3':
                print('Conta: Plus\n')

            contador = 0                                                                                           # Contador para verificar o arquivo mais recente, com o Input CPF.
            contadorStr = str(contador)
            while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
                contador += 1
                contadorStr = str(contador)
            contador = int(contadorStr)
            contador = contador - 1
            contadorStr = str(contador)

            for contador in range(contador, -1, -1):                # Contador para dar Print em informações de arquivos, do mais recente ao mais antigo, com o Input CPF e Contador.
                contadorStr = str(contador)
                arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
                dados = arquivo.readlines()                                                                                     # Salva a informações para utilizar depois nessa def.
                valor = dados[3]
                valorAcao = dados[5]
                tipoAcao = dados[6]
                dataEhora = dados[7]
                tarifa = dados[8]
                valor = valor.rstrip('\n')
                valorAcao = valorAcao.rstrip('\n')
                tipoAcao = tipoAcao.rstrip('\n')
                dataEhora = dataEhora.rstrip('\n')
                tarifa = tarifa.rstrip('\n')

                if tipoAcao == 'Debito':                                                                                                             # Verifica se a ação foi Débito.
                    print('%s | - %s ; Tarifa: %s ➔  Saldo: %s' %(dataEhora, valorAcao, tarifa, valor))
                elif tipoAcao == 'Deposito' or tipoAcao == 'Criar Conta':                                                           # Verifica se a ação foi Deposito ou Criar conta.
                    print('%s | + %s ; Tarifa: %s ➔  Saldo: %s' %(dataEhora, valorAcao, tarifa, valor))
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')                                                          # Define erro caso CPF e/ou senha estiverem incorretos.
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def main():                                                                                                                                                                # ★ Menu:

    while True:
        print('Banco QuemPoupaTem™')
        print('\n☆︵‿︵‿︵『Menu』‿︵‿︵‿☆\n')                                                                                                        # Mostra as opções do banco.

        print('1 - Criar nova conta')
        print('2 - Apagar conta')
        print('3 - Debitar')
        print('4 - Deposito')
        print('5 - Saldo')
        print('6 - Extrato')

        escolha = input('\nEscolha uma das opções acima: ')

        if escolha == '1':                                                                                                                   # Verifica se a ação é Criar nova conta.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Criar nova conta』★\n')
            criarConta()                                                                                                                               # Aciona a função: criarConta.

        if escolha == '2':                                                                                                                       # Verifica se a ação é Apagar conta.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Apagar conta』★\n')
            apagarConta()                                                                                                                             # Aciona a função: apagarConta.

        if escolha == '3':                                                                                                                            # Verifica se a ação é Debitar.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Debitar』★\n')
            debitar()                                                                                                                                     # Aciona a função: debitar.

        if escolha == '4':                                                                                                                          # Verifica se a ação é Depositar.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Depositar』★\n')
            depositar()                                                                                                                                 # Aciona a função: depositar.

        if escolha == '5':                                                                                                                              # Verifica se a ação é Saldo.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Saldo』★\n')
            saldo()                                                                                                                                         # Aciona a função: saldo.

        if escolha == '6':                                                                                                                            # Verifica se a ação é Extrato.
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Extrato』★\n')
            extrato()                                                                                                                                     # Aciona a função: extrato.
main()