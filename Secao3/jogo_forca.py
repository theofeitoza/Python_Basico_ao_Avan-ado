from os import system
palavra_secreta='casamento'
letras_acertadas=''
tentativas=0
while True:
    tentativas+=1
    letra_digitada=str(input('Digite uma letra: '))
    if len(letra_digitada)>1:
        print('Por favor, digite apenas uma letra')
        continue
    if letra_digitada in letras_acertadas:
        print('Digite uma letra não acertada')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas+=letra_digitada

    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada+='*'
    print(palavra_formada)

    if palavra_formada==palavra_secreta:
        system('cls')
        print('PARABÉNS, VOCÊ GANHOU O JOGO')
        print(f'A palavra era, {palavra_secreta}')
        print(f'Você precisou de {tentativas} tentativas para acertar')
        break