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

solution = Solution()
result = solution.climbStairs(5)
print(result)  # Salida: 8