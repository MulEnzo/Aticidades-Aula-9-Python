arquivo_1 =  open('arquivo_existente.txt', 'r', encoding='utf-8')

linhas = arquivo_1.readlines()

arquivo_1.close()

print("Linhas:", linhas)