def receber_dicionario(lista_1, lista_2):
    dicionario = {}
    for keys, valeus in zip(lista_1, lista_2):
        dicionario[keys] = valeus 

    return dicionario
