class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(1, len(triangle)):
            prev = list(zip([float('inf')] + triangle[i-1], triangle[i-1] + [float('inf')]))
            
            for j in range(len(triangle[i])):
                triangle[i][j] += min(prev[j])
                
        return min(triangle[-1])
    