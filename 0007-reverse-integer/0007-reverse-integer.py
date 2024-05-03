class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        while x > 0:
            last_dig = x % 10
            x = x // 10
            output = output * 10 + last_dig
        output *= sign
       
        if output < -2**31 or output > 2**31 - 1:
            return 0
        return output
