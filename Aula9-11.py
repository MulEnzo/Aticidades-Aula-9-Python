with open("texto.txt", "r", encoding="utf-8") as arq:

    print("\n")

    print("Posição:", arq.tell())
    primeira_linha = arq.readline()
    print(primeira_linha)

    print("Posição:", arq.tell())
    segunda_linha = arq.readline()
    print(segunda_linha)

    print("Posição:", arq.tell())
    terceira_linha = arq.readline()
    print(terceira_linha)