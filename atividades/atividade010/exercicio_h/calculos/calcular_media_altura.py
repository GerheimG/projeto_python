def calcular_media_altura(lista_clientes):
    # Somando todas as alturas
    somar_altura = sum(cliente['Altura'] for cliente in lista_clientes)
    # Calculando a média
    media = somar_altura / len(lista_clientes)
    return media