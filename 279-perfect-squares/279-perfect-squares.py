class Solution:
    def numSquares(self, n: int) -> int:
#         dp = [0] + [float('inf')]*n
#         for i in range(1, n+1):
#             dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
#         return dp[-1]
        
        
        dp = [0] + [n] * (n)
        
        for target in range(1, n+1):
            for j in range(1, int(target**0.5) + 1):
                square = j * j
                dp[target] = min(dp[target], dp[target-square] + 1)
                    
        return dp[-1]
