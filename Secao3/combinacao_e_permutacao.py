from itertools import combinations
from itertools import permutations
from itertools import product

#pessoas=['João','Joana','Luiz','Leticia']
#print(*list(combinations(pessoas,2)),sep='\n')


#pessoas=['João','Joana','Luiz','Leticia']
#print(*list(permutations(pessoas,2)),sep='\n')


camisetas=[['preta','branca'],['P','M','G'],]
print(*list(product(*camisetas)), sep='\n')