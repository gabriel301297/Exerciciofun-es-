#Faça um programa para imprimir:
def imprime(n):
    """Funcao que retorna P se o valor informado for > que 0 e N se for <."""
    if n > 0:
        print('P')
    elif n <= 0:
        print('N')
    return imprime


imprime(1)