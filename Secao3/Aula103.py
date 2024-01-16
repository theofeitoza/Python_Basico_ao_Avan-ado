from random import randint
contador=0
cpf_criado=''
for contador in range(9):
    cpf_criado+=str(randint(0,9))
    contador+=1
print(cpf_criado)

contador_regressivo_1=10
resultado_digito_1=0

for digito in cpf_criado:
    resultado_digito_1+=int(digito)*contador_regressivo_1
    contador_regressivo_1-=1
digito_1=((resultado_digito_1*10)%11)
digito_1=digito_1 if digito_1<=9 else 0
print(digito_1)

dez_digitos=cpf_criado+str(digito_1)
contador_regressivo_2=11
resultado_digito_2=0
for digito in dez_digitos:
    resultado_digito_2+=int(digito)*contador_regressivo_1
    contador_regressivo_2-=1
digito_2=((resultado_digito_2*10)%11)
digito_2=digito_2 if digito_2<=9 else 0
print(digito_2)
novo_cpf=f'{cpf_criado}{digito_1}{digito_2}'
print(novo_cpf)