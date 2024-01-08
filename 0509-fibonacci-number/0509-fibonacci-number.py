from math import sqrt as s
class Solution:
    def fib(self, n: int) -> int:
        # if(n==0 or n==1):
        #     return n
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
        phi= (s(5)+1)/2
        return int(((phi**n)-((-phi)**(-1*n)))/s(5))
        