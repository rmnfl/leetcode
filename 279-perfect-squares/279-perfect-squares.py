class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3
#         dp = [0] + [float('inf')]*n
#         for i in range(1, n+1):
#             dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
#         return dp[-1]
        
        
#         dp = [n] * (n+1)
#         dp[0] = 0
        
#         for target in range(1, n+1):
#             for j in range(1, int(target**0.5) + 1):
#                 square = j * j
#                 dp[target] = min(dp[target], dp[target-square] + 1)
                    
#         return dp[-1]
