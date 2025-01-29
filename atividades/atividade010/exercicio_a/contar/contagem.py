def listar_numero():
    lista_par = []
    lista_impar = []
    # Descobrir quais são pares ou ímpares
    lista = (1,2,3,4,5,6,7,8,9,10)
    for n in lista:
        if n % 2 == 0:
            lista_par.append(n)
        else:
            lista_impar.append(n)
        # Contando os pares e ímpares
        quantidade_par = len(lista_par)
        quantidade_impar = len(lista_impar)
        lista = (1,2,3,4,5,6,7,8,9,10)
    
    return lista_par, lista_impar, quantidade_par, quantidade_impar