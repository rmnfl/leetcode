class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive = negative = 0
        max_len = 0
        
        for n in nums:
            if n > 0:
                positive, negative = positive + 1, negative + 1 if negative else 0
            elif n < 0:
                positive, negative = negative + 1 if negative else 0, positive + 1
            else:
                positive = negative = 0
                
            max_len = max(max_len, positive)
            
        return max_len