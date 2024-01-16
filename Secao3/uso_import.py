import importlib

import Aula156_m

print(Aula156_m.variavel)

for i in range(10):
    importlib.reload(Aula156_m)
print('Fim')