class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n < 0:
                return helper(1 / x, -n)
            if n % 2 == 0:
                return helper(x * x, n // 2)
            else:
                return x * helper(x * x, (n - 1) // 2)

        return helper(x, n)
        
        