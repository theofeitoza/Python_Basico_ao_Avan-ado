produto={
	'nome':'Caneta Azul',
	'preço':2.5,
	'categoria':'Escritório'
}

dc={
	chave:valor.upper()
	if isinstance(valor,str) else valor
	for chave, valor
	in produto.items()
}

print(dc)