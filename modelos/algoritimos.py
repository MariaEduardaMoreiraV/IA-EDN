# algoritimo
def busca(lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i + 1
        return -1
    nomes = ["maria", "ana", "joao"]
    posição = busca(nomes)
    nome_procurado = input("Esta em busca de quem? ", nomes)
    print(" está na posição: ", posição)