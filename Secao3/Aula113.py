def multiplicar(*args):
    multiplicação=1
    for numero in args:
        multiplicação*=numero
    return(multiplicação)

multiplicação=multiplicar(1,2,3,4,5)
print(multiplicação)

def parouimpar(numero):
    if numero%2==0:
        return f'{numero} é par'
    return f'{numero} é impar'

print(parouimpar(2))