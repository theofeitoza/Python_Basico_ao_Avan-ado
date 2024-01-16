string='Théo'
metodo='upper'

if hasattr(string,'upper'):
    print('Existe upper')
    print(getattr(string,metodo)())