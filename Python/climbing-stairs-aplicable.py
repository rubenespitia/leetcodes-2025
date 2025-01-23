class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        
        # Usamos una tabla para calcular iterativamente
        dp = [0] * (n + 1)
        dp[0] = 1  # Una forma de llegar a 0
        dp[1] = 1  # Una forma de llegar a 1 (1)
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Sumas de 1 y 2
        
        return dp[n]

# Solicitar el número de escalones al usuario
try:
    n = int(input("Ingrese el número de escalones: "))
    solution = Solution()
    result = solution.climbStairs(n)
    print(f"El número de formas de llegar al escalón {n} es: {result}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


"""
Explicacion y contexto del problema

Se busca en primer lugar un numero n de escalones
Estos escalones los puedes subir en 1 o 2 pasos

Se busca imprimir el numero de posibilidades que esto tiene

Hay una formula lopgica que se puede aplicar, haciendo similitud a la secuencia de Fibonacci:
                            dp(n)=dp(n−1)+dp(n−2)

Donde:
dp(n) es el numero de formas de llegar al escalon n

dp(n-1) es el numero de formas de llegar al escalon sumando 1

dp(n-2) es el numero de formas de llegar al escalon sumando 2

Condiciones Iniciales:

dp(0) = 1 Hay una forma de estar en el suelo (sin subir escalones)
dp(1) = Hay una forma de llegar al primer escalon (subiendo 1 escalon)

La formula Recursiva General se describe como:

                        dp(n)=dp(n−1)+dp(n−2),para n≥2


Ejemplo n=7:

dp(7) = dp(6)+dp(5)

dp(6) = 13 dp(5)=8
dp(7) = 13+ 8= 21

Dando como resultado 21


url del problema:https://leetcode.com/problems/climbing-stairs/submissions/1517436537/?envType=problem-list-v2&envId=dynamic-programming
"""