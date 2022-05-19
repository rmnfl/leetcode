class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        max_value = 0
            
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1 if matrix[i][j] == "1" else 0
                max_value = max(max_value, dp[i+1][j+1])
                
        return max_value**2
        