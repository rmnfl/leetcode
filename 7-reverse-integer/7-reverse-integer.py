class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        
        if 2**31 - 1 > res > -2**31:
            if x < 0:
                return -res
            else:
                return res
        else:
            return 0