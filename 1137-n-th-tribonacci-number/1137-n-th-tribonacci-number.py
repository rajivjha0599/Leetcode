class Solution:
    def tribonacci(self, n: int) -> int:
        prev0 = 1
        prev1 = 1
        prev2 = 0
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3,n+1):
            dp = prev0 + prev1 + prev2
            prev2 = prev1
            prev1 = prev0
            prev0 = dp
        return dp
        