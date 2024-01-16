num=input('Digite um numero inteiro:')
try:
    num_int=int(num)    
    if num_int%2==0:
        print(f'{num} é um número par')
    else:
        print(f'{num} é um número impar')
except:
    print('O número digitado não é um inteiro')


entrada=input('Que horas são?')
try:
    hora = int(entrada)

    if hora>=0 and hora<=11:
        print('Bom dia')
    elif hora>11 and hora<=17:
        print('Boa tarde')
    elif hora>17 and hora<=23:
        print('Boa noite')
except :
    print('O número digitado não é um inteiro')


nome=input('Digite seu nome: ')
tamanho_nome=len(nome)
if tamanho_nome>1:
    if tamanho_nome<=4:
        print('Seu nome é curto')
    elif tamanho_nome<=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite mais de uma letra')