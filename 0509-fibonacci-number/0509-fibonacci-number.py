class Solution:
    def fib(self, n: int) -> int:
        cache = dict()
        cache[0] = 0
        cache[1] = 1

        def rec(n):
            nonlocal cache
            if n in cache:
                value = cache[n]
            else:
                value = rec(n-1) + rec(n-2)
                cache[n] = value
            return value
        
        return rec(n)
