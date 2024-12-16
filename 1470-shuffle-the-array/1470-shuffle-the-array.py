class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        result = []

        for _ in range(n):
            result.extend([nums[i], nums[j]])
            i += 1
            j += 1

        return result