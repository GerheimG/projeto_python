def aluno():

    dicionario = {}
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ')
    matricula = int(input('Insira o número de matrícula: '))
    data = input('Insira a data de nascimento (dd/mm/yy):  ')

    dicionario['Nome'] = nome
    dicionario['Matricula'] = matricula
    dicionario['Data'] = data


    return dicionario