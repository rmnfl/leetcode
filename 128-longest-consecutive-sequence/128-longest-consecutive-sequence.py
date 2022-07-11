class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        length = 1;
        longest_sequence = 1;
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                length += 1
            else:
                length = 1
            longest_sequence = max(longest_sequence, length)
            
        return longest_sequence
