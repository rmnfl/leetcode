class Solution:
    tri_res = {
        0: 0,
        1: 1,
        2: 1,
    }
    
    def tribonacci(self, n: int) -> int:
        if n in self.tri_res:
            return self.tri_res[n]
        else:
            res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.tri_res[n] = res
            return res
