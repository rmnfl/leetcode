class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_max_sum = best_min_sum = nums[0]
        
        max_cur_sum = min_cur_sum = 0
        
        for n in nums:
            max_cur_sum = max(max_cur_sum + n, n)
            min_cur_sum = min(min_cur_sum + n, n)
            
            best_max_sum = max(best_max_sum, max_cur_sum)
            best_min_sum = min(best_min_sum, min_cur_sum)
            

        if sum(nums)==best_min_sum:
            return best_max_sum
        
        return max(best_max_sum, sum(nums)-best_min_sum)