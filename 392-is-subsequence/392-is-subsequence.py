class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r1, r2 = len(t)-1, len(s)-1
        
        while r1 >= 0 and r2 >= 0:
            if t[r1] == s[r2]:
                r2 -= 1
            r1 -= 1
            
        return r2 < 0
