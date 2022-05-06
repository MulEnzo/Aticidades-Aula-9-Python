while True:

    print('\n\n--------- Menu ------------')

    print('  1 - Imprimir o saldo financeiro da empresa')
    print('  2 - Incluir novo registro (valor, descrição) no arquivo')
    print('  3 - Sair')

    opcao = input('\n  Digite sua opção: ')

    if opcao == '1':
        with open('financeiro.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        linhas = conteudo.split('\n')
        saldo = 0
        for linha in linhas:
            fragmentos = linha.split("\t")
            valor = float(fragmentos[0])
            print("Valor:", valor)
            print("Descrição:", fragmentos[1])
            saldo+=valor
        print("\n\nSaldo:", saldo)
    elif opcao == '2':
        valor = float(input("Digite po valor:"))
        desc = input("Digite a descrição:")

        with open('financeiro.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'\n{str(valor)}\t{desc}')
    elif opcao == '3':
        print('\n\n  Saindo ....')
        break
    else:
        print('\n\n  Opção Inválida!')