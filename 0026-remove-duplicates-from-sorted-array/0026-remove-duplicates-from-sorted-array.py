class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        curr = 0

        while curr < len(nums):
            if nums[prev] != nums[curr]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1

        return prev + 1