import pickle
import os
import math


if __name__ == '__main__':

    lista_codigos = []
    produtos = []

    diretorio = "produtos.pkl"

    if os.path.exists(diretorio) == True:
        with open('produtos.pkl', 'rb') as arq:
            while True:
                try:
                    p = pickle.load(arq)
                    produtos.append(p)
                except EOFError:
                    break
        for p in produtos:
            lista_codigos.append(p[0])

        print(lista_codigos)

    while True:

        print('\n\nCADASTRO DE PRODUTOS\n')
        print('  1 - INSERIR UM NOVO PRODUTO')
        print('  2 - ALTERAR UM PRODUTO')
        print('  3 - EXCLUIR UM PRODUTO')
        print('  4 - EXCLUIR TODOS OS PRODUTOS')
        print('  5 - CONSULTAR UM PRODUTO')
        print('  6 - LISTAR TODOS OS PRODUTOS')
        print('  7 - EXIBIR DADOS ESTATÍSTICOS')
        print('  8 - SAIR')

        opcao = input('\nDigite sua opção: ')

        if opcao == "1":

            codigo = input('\n\nCódigo do produto: ')
            while True:
                if codigo in lista_codigos:
                    print('\nO código já está cadastrado em um produto')
                    codigo = input('\n\nCódigo do produto: ')
                    if codigo in lista_codigos:
                        continue
                    else:
                        break
                else:
                    break
            lista_codigos.append(codigo)
            nome = input('Nome do produto: ')
            qnt_est = int(input("Quantidade do produto em estoque: "))
            preco = float(input("Preço do produto: "))
            produto = (codigo,nome,qnt_est,preco)
            produtos.append(produto)
            with open('produtos.pkl', 'ab') as arq:
                pickle.dump(produto, arq)
        
        elif opcao == "2":

            codigo_alterar = input("Digite o código do produto que deseja alterar: ")
            if codigo_alterar in lista_codigos:
                for i in range(len(produtos)):
                    for j in produtos:
                        if j[0] == codigo_alterar:
                            del produtos[i]
                codigo = codigo_alterar
                nome = input('Nome do produto: ')
                qnt_est = int(input("Quantidade do produto em estoque: "))
                preco = float(input("Preço do produto: "))
                produto = (codigo,nome,qnt_est,preco)
                produtos.append(produto)
                with open('produtos.pkl', 'wb') as arq:
                    for i in range(len(produtos)):
                        pickle.dump(produtos[i], arq)
            else:
                print("\nO código digitado não está listado em nenhum produto\n")
        
        elif opcao == "3":
            codigo_excluir = input("Digite o código do produto que deseja excluir: ")
            if codigo_excluir in lista_codigos:
                lista_codigos.remove(codigo_excluir)
                for i in range(len(produtos)):
                    for j in produtos:
                        if j[0] == codigo_excluir:
                            del produtos[i]
                with open('produtos.pkl', 'wb') as arq:
                    for i in range(len(produtos)):
                        pickle.dump(produtos[i], arq)
            else:
                print("\nO código digitado não está listado em nenhum produto\n")
        
        elif opcao == "4":

            lista_codigos = []
            with open('produtos.pkl', 'wb') as arq:
                print("\nOs produtos foram excluídos do arquivo\n")
        
        elif opcao == "5":

            soma=0
            codigo_consultar = input("Digite o código do produto que deseja consultar: ")
            produtos = []
            with open('produtos.pkl', 'rb') as arq:
                while True:
                    try:
                        p = pickle.load(arq)
                        produtos.append(p)
                    except EOFError:
                        break
            for p in produtos:
                if p[0] == codigo_consultar:
                    print('\nCódigo:', p[0])
                    print('Nome:', p[1])
                    print('Quantidade do produto:', p[2])
                    print('Preço do produto:', p[3])
                else:
                    soma+=1
                    if soma == len(produtos):
                        print("\nO código do produto não foi encontrado no arquivo\n")
        
        elif opcao == "6":

            if len(lista_codigos) > 0:
                produtos = []
                with open('produtos.pkl', 'rb') as arq:
                    while True:
                        try:
                            p = pickle.load(arq)
                            produtos.append(p)
                        except EOFError:
                            break
                for p in produtos:
                    print('\nCódigo:', p[0])
                    print('Nome:', p[1])
                    print('Quantidade do produto:', p[2])
                    print('Preço do produto:', p[3])
            else:
                print("\nNão há nenhum produtrado no arquivo\n")

        elif opcao == "7":

            est_baixo = 0
            soma_qnt_prod = 0
            acima_media = 0
            media_precos = 0
            dp = 0
            var = 0.0

            print("\nTotal de produtos cadastrados:", len(produtos))

            for p in produtos:
                soma_qnt_prod += p[2]
                if p[2] <= 20:
                    est_baixo += 1
            print("\nQuantidade de produtos com estoque baixo: {} --- Percentual de produtos com estoque baixo: {} %" .format(est_baixo,est_baixo*100/len(produtos)))
            
            media_qnt_prod = soma_qnt_prod/len(produtos)
            for p in produtos:
                if p[2] > media_qnt_prod:
                    acima_media += 1
            print("\nQuantidade de produtos acima da média: {} --- Percentual de produtos acima da média: {} %" .format(acima_media,acima_media*100/len(produtos)))
            
            for p in produtos:
                media_precos += p[3]
            media_precos = media_precos/len(produtos)

            for p in produtos:
                var+= (p[3]-media_precos)**2

            dp = math.sqrt(var)

            print("\nMédia geral dos preços dos produtos cadastrados: {:.2f} --- Desvio padrão dos preços dos produtos: {:.2f}" .format(media_precos,dp))

        elif opcao == "8":

            print('\n Encerrando o sistema ...\n')
            break

        else:
            
            print('\n  Opção Inválida!\n')