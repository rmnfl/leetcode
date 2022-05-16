class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1 
        p2, p3, p5 = 0, 0, 0
        
        for i in range(1, n):
            num = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            dp[i] = num
            
            if dp[p2]*2 == num:
                p2 += 1
            if dp[p3]*3 == num:
                p3 += 1
            if dp[p5]*5 == num:
                p5 += 1
            
        return dp[-1]