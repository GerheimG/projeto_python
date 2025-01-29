# Função para exibir os resultados
def exibir_reultado(acertos, qntd_perguntas):
    print('-'*70)
    print(f'Você acertou a capital de {acertos} estados(s).')
    print('-'*70)
    print(f'Resultado: {acertos}/{qntd_perguntas}\n')
    return acertos, qntd_perguntas
