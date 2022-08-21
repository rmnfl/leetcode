class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        chars = {}
        
        for i, char in enumerate(s):
            if char in chars and left <= chars[char]:
                left = chars[char] + 1
            else:
                max_len = max(max_len, i - left + 1)
                
            chars[char] = i
        
        return max_len
    