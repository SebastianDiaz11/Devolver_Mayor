"""
1. Definir una funcion max()que tome como argumento dos numeros y devuelva el mayor de ellos.
(Es cierto que python tiene una funcion max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.)
"""


def custom_max(n1: int,n2: int):
    """Dado dos numeros de entrada retorna el maximo de ambos

    Args:
        n1(int): Primer numero a comparar
        n2(int): Segundo numero a comparar

    Returns:
        int: Mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    raise Exception("Algo salio mal")

print(custom_max(800,600))
print(custom_max(-100,9))
print(custom_max(10, 10))
