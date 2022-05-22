class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        
        for target in range(1, n+1):
            dp[target] = min(dp[target-j * j] for j in range(1, int(target**0.5) + 1)) + 1
                    
        return dp[-1]