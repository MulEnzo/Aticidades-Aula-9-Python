arquivo = open("texto.txt", "r", encoding="utf-8")

primeira_linha = arquivo.readline()

print(primeira_linha)

segunda_linha = arquivo.readline()

print(segunda_linha)

arquivo.close()