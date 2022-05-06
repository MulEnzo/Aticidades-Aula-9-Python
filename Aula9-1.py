arquivo_1 =  open('arquivo_existente.txt', 'r')

print(type(arquivo_1))

arquivo_2 = open('novo_arquivo.txt', 'w')

print(type(arquivo_2))

arquivo_3 = open('novo_arquivo.txt', 'r+')

print(type(arquivo_3))

arquivo_4 = open('novo_arquivo.txt', 'a')

print(type(arquivo_4))