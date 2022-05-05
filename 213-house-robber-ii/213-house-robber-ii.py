class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.simpleRob(nums[:-1]), self.simpleRob(nums[1:]))
    
    def simpleRob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        
        return prev1
