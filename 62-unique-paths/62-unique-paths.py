class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tiles = [[0 for _ in range(n+1)] for _ in range(m+1)]
        tiles[1][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                tiles[i][j] += tiles[i-1][j] + tiles[i][j-1]
                
        return tiles[-1][-1]