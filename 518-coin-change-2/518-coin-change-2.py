class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for i in range(len(coins)-1, -1, -1):
            new_dp = [0] * (amount+1)
            new_dp[0] = 1
            
            for j in range(amount+1):
                new_dp[j] = dp[j]
                if j - coins[i] >= 0:
                    new_dp[j] += new_dp[j - coins[i]]
            dp = new_dp
            
        return dp[-1]
        