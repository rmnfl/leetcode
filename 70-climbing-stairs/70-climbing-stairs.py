class Solution:
    stairs_dic = {
        1: 1,
        2: 2
    }
    
    def climbStairs(self, n: int) -> int:
        if n in self.stairs_dic:
            return self.stairs_dic[n]
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.stairs_dic[n] = res
            return res
    