pessoa={'nome':'Théo','sobrenome':'Lima','idade':'20','endereço':{'Rua':'Olivio Andrade Ribeiro','N.':'118','Bairro':'Jardim Primavera'}}

#for chave in pessoa:
#    print(chave,pessoa[chave])

chave='Tamanho'
pessoa[chave]='1.88'
del pessoa['endereço']
print(pessoa)