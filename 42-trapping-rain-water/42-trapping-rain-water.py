class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        ans = 0
        
        
        left_max[0] = height[0]
        for i, h in list(enumerate(height))[1:]:
            left_max[i] = max(left_max[i-1], h)
        
        right_max[-1] = height[-1]
        for i, h in list(enumerate(height))[-2::-1]:
            right_max[i] = max(right_max[i+1], h)
            
        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans