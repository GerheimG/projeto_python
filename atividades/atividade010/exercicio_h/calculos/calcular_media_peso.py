def calcular_media_peso(lista_clientes):
    # Somando todos os pesos
    somar_peso = sum(cliente['Peso'] for cliente in lista_clientes)
    # Calculando a média
    media = somar_peso / len(lista_clientes)
    return media