class Solution(object):
    def stableMountains(self, height, threshold):
        arrayResult = [];

        for i in range(len(height)):
            if (i > 0 and height[i-1]>threshold):
               arrayResult.append(i)


        return arrayResult


try:
    solution = Solution()
    result = solution.stableMountains([10,1,10,1,10],5)
    print(f"Las montanias estables son: {result}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


#LeetCode Python
"""
Complejidad Temporal
La complejidad temporal de esta funcion depende principalmente de los siguientes factores
1.- El bucle for:
    El bucle itera a travez de todos los elementos en la lista height. Si la longitud de 
    Height es n, el bucle realiza n iteraciones
    
    En cada iteracion, se realizan dos comparaciones:
    i>0
    height{i-1}> threshold

    Ambas son operaciones constantes, es decir, tienen una complejidad de O(1) por iteracion

2.-El metodo append() de una lista en python tiene una complejidad amortizada de O(1) por operacion, ya que, en la mayoria de los casos,
    simplemente agrega un elemento al final

Complejidad Total
Por lo tanto la complejidad temporal total de la funcion es O(n), donde n es el numero
de elementos en la lista height.

Complejidad Espacial:
Se usa un arreglo adicional arrayResult para almacenar los indicies que cumplen con la condicion
En el peor caso, si todos los elementos cumplen la condicion el tamanio de ArrayResult puede ser igual al
tamanio de height, lo que significa que la complejidad espacial es O(n)

"""