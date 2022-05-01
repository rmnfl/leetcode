class Solution:
    fib_res = {}
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in self.fib_res:
                return self.fib_res[n]
            else:
                res = self.fib(n-1) + self.fib(n-2)
                self.fib_res[n] = res
                return res