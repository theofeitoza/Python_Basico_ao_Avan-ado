import re
import sys
cpf_enviado=str(input('Digite o seu CPF: '))
cpf_enviado=re.sub(r'[^0-9]','',cpf_enviado)

entrada_sequencial=cpf_enviado==cpf_enviado[0]*len(cpf_enviado)
if entrada_sequencial:
    sys.exit()
    
nove_digitos=cpf_enviado[:9]
contador_regressivo_1=10
resultado_digito_1=0

for digito in nove_digitos:
    resultado_digito_1+=int(digito)*contador_regressivo_1
    contador_regressivo_1-=1
digito_1=((resultado_digito_1*10)%11)
digito_1=digito_1 if digito_1<=9 else 0

dez_digitos=nove_digitos+str(digito_1)
contador_regressivo_2=11
resultado_digito_2=0
for digito in dez_digitos:
    resultado_digito_2+=int(digito)*contador_regressivo_1
    contador_regressivo_2-=1
digito_2=((resultado_digito_2*10)%11)
digito_2=digito_2 if digito_1<=9 else 0

novo_cpf=f'{nove_digitos}{digito_1}{digito_2}'
if novo_cpf==cpf_enviado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')