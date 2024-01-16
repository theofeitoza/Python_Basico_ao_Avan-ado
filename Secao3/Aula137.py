produtos=[{'nome':'p1','preço':20},{'nome':'p1','preço':10},{'nome':'p1','preço':30}]
novos_produtos=[{**produto,'preço':produto['preço']*1.05}for produto in produtos]

print(*novos_produtos, sep='\n')