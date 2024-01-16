produtos=[{'nome':'p1','preço':20},{'nome':'p1','preço':10},{'nome':'p1','preço':30}]
novos_produtos=[
	{**produto,'preço':produto['preço']*1.05}
	if produto['preço']>20 else {**produto}
	for produto in produtos
	if (produto['preço']*1.05)>10
]
print(*novos_produtos, sep='\n')