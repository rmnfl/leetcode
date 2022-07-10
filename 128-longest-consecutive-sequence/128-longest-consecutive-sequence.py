class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        
        max_len = 0
        
        while nums:
            n = nums.pop()
            
            l = n - 1
            r = n + 1
            
            while l in nums:
                nums.remove(l)
                l -= 1
                
            while r in nums:
                nums.remove(r)
                r += 1
            
            max_len = max(max_len, r-l-1)   
            
        return max_len
    