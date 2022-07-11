class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = height[0], height[-1]
        l, r = 0, len(height) - 1
        result = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] < left_max:
                    result += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if height[r] < right_max:
                    result += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1
    
        return result