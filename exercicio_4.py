import pickle


if __name__ == '__main__':

    while True:

        print('\n\nCadastro Alunos\n')
        print('  1 - Cadastrar Aluno')
        print('  2 - Listar Alunos')
        print('  3 - Sair')

        opcao = input('\nDigite sua opção: ')

        if opcao == '1':
            nome = input('\n\n  Nome: ')
            cpf = input('  CPF: ')
            aluno = (nome, cpf)
            with open('alunos.pkl', 'ab') as arq:
                pickle.dump(aluno, arq)
        elif opcao == '2':
            alunos = []
            with open('alunos.pkl', 'rb') as arq:
                while True:
                    try:
                        aluno = pickle.load(arq)
                        alunos.append(aluno)
                    except EOFError:
                        break
            print('\n\n  Total alunos:', len(alunos))
            for aluno in alunos:
                print('\n  Nome:', aluno[0])
                print('    CPF:', aluno[1])
        elif opcao == '3':
            print('\n\n Encerrando o sistema ...')
            break
        else:
            print('\n\n  Opção Inválida!')