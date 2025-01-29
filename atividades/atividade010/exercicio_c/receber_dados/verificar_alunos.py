def verificar_aluno(resultado):



    pergunta = input('Qual aluno irá verificar? ').capitalize().strip()
    
    # Verificando se o aluno está na lista
    for aluno in resultado:
        if aluno['Nome'] == pergunta:
            print('Nome: ', aluno['Nome'])
            print('Matrícula: ', aluno['Matricula'])
            print('Data de Nascimento: ', aluno['Data'])
            break
    else:
        print('Aluno não está cadastrado.')
        