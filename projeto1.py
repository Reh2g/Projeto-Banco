from datetime import datetime, timedelta
import os

def criarConta():
    nome = input('Digite seu nome: ')
    cpfReal = int(input('Digite seu CPF: '))
    cpf = str(cpfReal)
    senhaReal = int(input('Digite uma senha (apenas números): '))
    senha = str(senhaReal)
    valor = float(input('Digite o valor inicial da conta: '))
    print('\n1 = Salário: \n● Cobra taxa de 5% a cada débito realizado;\n● Não permite débitos que deixem a conta com saldo negativo.')
    print('\n2 = Comum \n● Cobra taxa de 3% a cada débito realizado;\n● Permite um saldo negativo de até (R$ 500,00).')
    print('\n3 = Plus \n● Cobra taxa de 1% a cada débito realizado;\n● Permite um saldo negativo de até (R$ 5.000,00).')
    tipo = input('\nEscolha um dos tipos de conta acima: ')

    if tipo != '1' and tipo != '2' and tipo != '3':
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Esse tipo não é uma opção oferecida pelo banco...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    elif os.path.isfile(cpf + '(0)' + '.txt'):
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Esse CPF já foi registrado...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        arquivo = open(cpf + '(0)' + '.txt', 'w')
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

def apagarConta():
    confirmaCPF = input('Digite seu CPF: ')

    contador = 0
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()
        confirmaSenha = dados[2]
        confirmaSenha = confirmaSenha.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')
        if senhaInput == confirmaSenha:
            confirmacao = input('Digite sua senha para prosseguir (DELETAR SUA CONTA É UMA AÇÃO IRREVERSÍVEL): ')
            if confirmacao == senhaInput:
                contadorDel = contador
                for contadorDel in range(contadorDel, -1, -1):
                    contadorStrDel = str(contadorDel)
                    os.remove(confirmaCPF + '(' + contadorStrDel + ')' + '.txt')
                print('\n★ Conta deletada com sucesso!\n')
                input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def debitar():
    confirmaCPF = input('Digite seu CPF: ')

    contador = 0
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()
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
        senhaInput = input('Digite sua senha: ')
        if senhaInput == confirmaSenha:
            valorDebitar = float(input('Digite o valor que você deseja retirar: '))
            if tipo == '1':
                tarifa = (valorDebitar * 5) / 100
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < 0:
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 0,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + contadorStr + '.txt'):
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')
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
            elif tipo == '2':
                tarifa = (valorDebitar * 3) / 100
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < -(500):
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 500,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + contadorStr + '.txt'):
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')
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
            elif tipo == '3':
                tarifa = (valorDebitar * 1) / 100
                valorNovo = valorInicial - valorDebitar
                valorNovo = valorNovo - tarifa
                if valorNovo < -(5000):
                    print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
                    print('\nImpossível fazer operação, pois seu novo saldo será menor que R$ 5.000,00')
                    input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
                else:
                    contador = 1
                    contadorStr = str(contador)
                    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
                        contador += 1
                        contadorStr = str(contador)

                    arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')
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
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def depositar():
    confirmaCPF = input('Digite seu CPF: ')

    contador = 0
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()
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
        valorDepositar = float(input('Digite a quantia que você deseja depositar: '))
        valorNovo = valorInicial + valorDepositar

        contador = 1
        contadorStr = str(contador)
        while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
            contador += 1
            contadorStr = str(contador)

        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'w')
        data = datetime.now()
        arquivo.write('%s\n' % nome)
        arquivo.write('%s\n' % confirmaCPF)
        arquivo.write('%s\n' % confirmaSenha)
        arquivo.write('%.2f\n' % valorNovo)
        arquivo.write('%s\n' % tipo)
        arquivo.write('%.2f\n' % valorDepositar)
        arquivo.write('Deposito')
        arquivo.write(data.strftime('\n%d/%m/%Y %H:%M:%S'))
        arquivo.write('0.00')
        arquivo.close()
        print('\n★ Dinheiro depositado com sucesso!\n')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! O CPF está incorreto...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def saldo():
    confirmaCPF = input('Digite seu CPF: ')

    contador = 0
    contadorStr = str(contador)
    while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        contador += 1
        contadorStr = str(contador)
    contador = int(contadorStr)
    contador = contador - 1
    contadorStr = str(contador)

    if os.path.exists(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
        arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
        dados = arquivo.readlines()
        confirmaSenha = dados[2]
        valor = dados[3]
        confirmaSenha = confirmaSenha.rstrip('\n')
        valor = valor.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')

        if senhaInput == confirmaSenha:
            print('\n★ Seu saldo atual é de: R$ %s\n' % valor)
            input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
        else:
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')
            input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def extrato():
    confirmaCPF = input('Digite seu CPF: ')
    if os.path.exists(confirmaCPF + '(0)' + '.txt'):
        arquivo = open(confirmaCPF + '(0)' + '.txt', 'r')
        dados = arquivo.readlines()
        nome = dados[0]
        confirmaSenha = dados[2]
        tipo = dados[4]
        nome = nome.rstrip('\n')
        confirmaSenha = confirmaSenha.rstrip('\n')
        tipo = tipo.rstrip('\n')
        arquivo.close()
        senhaInput = input('Digite sua senha: ')

        if senhaInput == confirmaSenha:
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿\n')
            print('Nome: %s' % nome)
            print('CPF: %s' % confirmaCPF)
            if tipo == '1':
                print('Conta: Salário')
            elif tipo == '2':
                print('Conta: Comum')
            elif tipo == '3':
                print('Conta: Plus\n')

            contador = 0
            contadorStr = str(contador)
            while os.path.isfile(confirmaCPF + '(' + contadorStr + ')' + '.txt'):
                contador += 1
                contadorStr = str(contador)
            contador = int(contadorStr)
            contador = contador - 1
            contadorStr = str(contador)

            for contador in range(contador, -1, -1):
                contadorStr = str(contador)
                arquivo = open(confirmaCPF + '(' + contadorStr + ')' + '.txt', 'r')
                dados = arquivo.readlines()
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

                if tipoAcao == 'Debito':
                    print('%s | - %s ; Tarifa: %s ➔  Saldo: %s' %(dataEhora, valorAcao, tarifa, valor))
                elif tipoAcao == 'Deposito' or tipoAcao == 'Criar Conta':
                    print('%s | + %s ; Tarifa: %s ➔  Saldo: %s' %(dataEhora, valorAcao, tarifa, valor))
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')
    else:
        print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
        print('\n¡ERRO! Seu CPF e/ou sua senha estão incorretos...')
        input('\n(Entre com qualquer tecla para voltar ao Menu)\n\n')

    print('\n︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')

def main():

    while True:
        print('Banco QuemPoupaTem™')
        print('\n☆︵‿︵‿︵『Menu』‿︵‿︵‿☆\n')

        print('1 - Criar nova conta')
        print('2 - Apagar conta')
        print('3 - Debitar')
        print('4 - Deposito')
        print('5 - Saldo')
        print('6 - Extrato')

        escolha = input('\nEscolha uma das opções acima: ')

        if escolha == '1':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Criar nova conta』★\n')
            criarConta()

        if escolha == '2':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Apagar conta』★\n')
            apagarConta()

        if escolha == '3':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Debitar』★\n')
            debitar()

        if escolha == '4':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Depositar』★\n')
            depositar()

        if escolha == '5':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Saldo』★\n')
            saldo()

        if escolha == '6':
            print('︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿')
            print('\n★ 『Extrato』★\n')
            extrato()
main()
