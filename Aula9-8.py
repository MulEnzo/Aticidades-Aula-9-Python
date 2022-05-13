with open("arquivo_existente.txt", "r", encoding="utf-8") as arq:
    linhas = arq.readlines()

print("\n")
print("Linhas:", linhas)
print("\n")

with open("novo_arquivo.txt", "w", encoding="utf-8") as arq:
    arq.write('Enzo')