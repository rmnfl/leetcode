class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()
        cache[1] = 1
        cache[2] = 2

        def rec(n: int) -> int:
            nonlocal cache

            if n in cache:
                value = cache[n]
            else:
                value = rec(n-1) + rec(n-2)
                cache[n] = value
            return value
        
        return rec(n)