with open("arquivo.bin","rb") as arq:
    linhas = arq.readlines()
    nome = linhas[0].decode()
    print("\nNome:", nome)
    lista = list(linhas[1])
    print("Lista:", lista)
    print("\n")