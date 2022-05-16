class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))
        
        for i in range(len(s) + 1):
            for j in range(i):
                if i-j > max_len:
                    continue
                if (dp[j] and s[j:i] in wordDict):
                    dp[i] = True
                    break
                    
        return dp[-1]
        