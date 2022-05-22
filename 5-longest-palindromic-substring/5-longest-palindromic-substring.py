class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = s[0]
        
        for i in range(len(s)):
            dp[i][i] = True
                
        for i in range(len(s), -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > len(ans):
                            ans = s[i:j+1]
        
        return ans