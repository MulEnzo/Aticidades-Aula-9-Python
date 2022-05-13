import os

dir_raiz = 'nova pasta/'

nomes_sub = os.listdir(dir_raiz)

for nome in nomes_sub:
    subdiretorio = os.path.join(dir_raiz, nome)
    novo_subdiretorio = os.path.join(dir_raiz, nome.lower())
    os.rename(subdiretorio, novo_subdiretorio)