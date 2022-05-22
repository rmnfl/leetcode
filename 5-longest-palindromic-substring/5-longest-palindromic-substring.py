class Solution:
    def longestPalindrome(self, s: str) -> str:           
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = s[0]
        
        for i in range(len(s)):
            dp[i][i] = True
                
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                        dp[i][j] = True
                        if len(ans) < j-i+1:
                            ans = s[i:j+1]
        
        return ans