class Solution:
    def countGoodNumbers(self, n: int) -> int:
        kmod = 1000000007
        def power(x,n):
            if n == 0:return 1
            if n == 1:return x%kmod
            
            pov = power(x,n//2)
            if n %2 == 1:
                return (x*pov*pov)%kmod
            else:
                return (pov*pov)%kmod
            
        even_half = n//2+n%2
        odd_half = n//2
        
        return (power(5,even_half)*power(4,odd_half))%kmod
