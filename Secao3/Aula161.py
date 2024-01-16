import copy

from Aula160 import produtos

novos_produtos= [
    {**p,'preco':round(p['preco']*1.1,2)}
    for p in copy.deepcopy(produtos)
]
produtos_ordenados_por_nome=sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

print(*produtos,sep='\n')
print()
print(*novos_produtos,sep='\n')
print()
print(*produtos_ordenados_por_nome,sep='\n')