class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = i if i<n else 0
            for j in range(i):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
                
        return dp[-1]
                