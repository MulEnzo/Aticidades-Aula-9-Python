texto = "Nome: Enzo Salamão Roseiro\nIdade: 19 anos"

arq = open('novo_arquivo', 'w', encoding='utf-8')

print(texto, file=arq)

arq.close()