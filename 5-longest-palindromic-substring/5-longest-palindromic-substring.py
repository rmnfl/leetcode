class Solution:
    def longestPalindrome(self, s: str) -> str:           
        dp = [[False]*len(s) for _ in range(len(s)) ]
        
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans
        
#         dp = [[False] * len(s) for _ in range(len(s))]
#         ans = s[0]
        
#         for i in range(len(s)):
#             dp[i][i] = True
                
#         for i in range(len(s)-1, -1, -1):
#             for j in range(i+1, len(s)):
#                 if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
#                         dp[i][j] = True
#                         if len(ans) < j-i+1:
#                             ans = s[i:j+1]
        
#         return ans