class Solution:
    def longestPalindrome(self, s: str) -> str:           
        ans = s[0]
        
        for i in range(len(s)):
            ans = max(ans, self.expandAroundCenter(s, i, i), self.expandAroundCenter(s, i, i+1), key = len)
            
        return ans
        
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
                
        return s[l+1:r]
