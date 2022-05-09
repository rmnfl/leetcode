class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        imax = imin = 1
        
        for n in nums:
            if n < 0:
                imax, imin = imin, imax
            
            imax = max(imax * n, n)
            imin = min(imin * n, n)
            
            max_product = max(max_product, imax)
        
        return max_product
    