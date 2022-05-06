with open('train.csv', 'r') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

linhas = linhas[1:]

dados = []

for linha in linhas:    
    fragmentos = linha.split(',')
    if len(fragmentos) > 1:
        dados.append(fragmentos)

print('\n\nDados:', dados)