class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = nums[0]
        
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            best_sum = max(cur_sum, best_sum)
            
        return best_sum
            