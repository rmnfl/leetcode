class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tiles = [[1 for _ in range(n)] for _ in range(m)]
        tiles[0][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                tiles[i][j] = tiles[i-1][j] + tiles[i][j-1]
                
        return tiles[-1][-1]
