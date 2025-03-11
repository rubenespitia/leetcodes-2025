class Solution(object):
    def esPalindromo(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        mitad_reversada = 0
        while x > mitad_reversada:
            mitad_reversada = mitad_reversada * 10 + x % 10
            x //= 10
        return x == mitad_reversada or x == mitad_reversada // 10

sol = Solution()
numero = -101
resultado = sol.esPalindromo(numero)
print(resultado)