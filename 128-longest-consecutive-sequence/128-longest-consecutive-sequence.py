class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        
        max_len = 0
        
        for n in nums:
            if n-1 not in nums:
                curr_num = n
                curr_len = 1
                
                while curr_num+1 in nums:
                    curr_len += 1
                    curr_num += 1
                
                max_len = max(max_len, curr_len)
            
        return max_len