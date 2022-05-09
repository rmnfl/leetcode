class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.Counter(nums)
            
        prev, curr = 0, 0
        for i in range(max(nums) + 1):
            prev, curr = curr, max(prev+points[i]*i, curr)
            
        return max(prev, curr)