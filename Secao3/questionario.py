perguntas=[
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['1','2','3','4','5'],
        'Resposta':'4'
    },
    {
        'Pergunta':'Quanto é 5*5',
        'Opções':['25','12','30','20','5'],
        'Resposta':'25'
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opções':['8','4','5','2','10'],
        'Resposta':'5'
    }
]
qtd_acertos=0
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])
    print()

    opcoes=pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha=input('Escolha uma opção: ')
    escolha_int=None
    quantidade_opcoes=len(opcoes)
    acertou=False

    if escolha.isdigit():
        escolha_int=int(escolha)
    
    if escolha_int is not None:
        if escolha_int>=0 and escolha_int<quantidade_opcoes:
            if opcoes[escolha_int]==pergunta['Resposta']:
                acertou=True

    if acertou:
        print('PARABÉNS, você acertou')
        qtd_acertos+=1
    else:
        print('Você errou')

    print()
print(f'Você acertou {qtd_acertos}',end='')
print('de', len(perguntas),'perguntas')