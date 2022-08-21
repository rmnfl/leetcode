class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        
        l = 0
        max_f = 0
        
        for r, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            max_f = max(max_f, count[char])
            
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                
            result = max(result, r - l + 1)
            
        return result