class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        prev = 0
        curr = 0

        while curr < len(nums):
            if nums[curr] != val:
                nums[prev] = nums[curr]
                prev += 1
            curr += 1

        return prev