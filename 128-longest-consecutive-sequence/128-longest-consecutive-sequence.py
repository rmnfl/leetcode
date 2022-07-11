class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in numSet:
                current_longest = 1
                found_max = False
                while not found_max:
                    num += 1
                    if num in numSet:
                        current_longest += 1
                    else:
                        found_max = True
                longest = max(longest, current_longest)
        
        return longest