with open("texto.txt", "r", encoding="utf-8") as arq:

    print("\n")

    print("Posição:", arq.tell())
    linha = arq.readline()
    print(linha)

    arq.seek(0)

    print("Posição:", arq.tell())
    linha = arq.readline()
    print(linha)