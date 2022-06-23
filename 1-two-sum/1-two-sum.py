class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        
        for i, n in enumerate(nums):
            if target - n in nums_dict:
                return [nums_dict[target - n], i]
            nums_dict[n] = i