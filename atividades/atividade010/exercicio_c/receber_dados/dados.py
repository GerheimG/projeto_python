def aluno():
    alunos_dict = {}

    alunos_lista = []
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ').capitalize().strip()
    matricula = int(input('Insira o número de matrícula: '))
    data = input('Insira a data de nascimento: ')

    # Colocando dentro da lista
    alunos_dict = {'Nome': nome, 'Matricula': matricula, 'Data': data}
    alunos_lista.append(alunos_dict)
    print(alunos_lista)
    return alunos_lista