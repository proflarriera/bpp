#import pdb
#pdb.set_trace()

"""
1. Haciendo uso de comprensión de listas realice un programa que, dado
una lista de listas de números enteros, devuelva el máximo de cada
lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
El programa debe devolver el mayor elemento de cada sublista
(señalado en negrita).
"""

lista_original = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

def lista_maximos(lista):
    maximos = []
    maximos = [max(i) for i in lista]
    return maximos

print("")
print("Ejercicio 1:")
print(f"El resultado de tomar los máximos de cada lista de la lista {lista_original}")
print(f"Es: {lista_maximos(lista_original)}")
print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


"""
2. Haga uso de la función filter para construir un programa que, dado
una lista de n números devuelva aquellos que son primos. Por
ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente
debe devolver como resultado [3, 5, 5, 13]
"""

lista_original = [3, 4, 8, 5, 5, 22, 13]

def es_primo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        return True

def lista_primos(lista):
    #return [i for i in lista if es_primo(i)]
    return list(filter(lambda i: es_primo(i), lista_original))

print("")
print("Ejercicio 2:")
print(f"Los números primos de la lista {lista_original}")
print(f"Son: {lista_primos(lista_original)}")
print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

