class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = cur_farthest = 0
        
        if len(nums) == 1:
            return 0
        
        for i, n in enumerate(nums):
            cur_farthest = max(cur_farthest, i + n)
            
            if i == cur_end:
                cur_end = cur_farthest
                jumps += 1
                
                if cur_farthest >= len(nums) - 1:
                    break
                
        return jumps
