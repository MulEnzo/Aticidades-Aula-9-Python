arquivo_1 =  open('arquivo_existente.txt', 'r', encoding='utf-8')

conteudo = arquivo_1.read()
# conteudo = arquivo_1.read(10) -> Faz a leitura dos 10 primeiros caracteres do arquivo.

arquivo_1.close()

print("Conteúdo:", conteudo)