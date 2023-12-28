from math import floor as f
class Solution(object):
    def intVal(self,num):
        ans=0
        num=num[::-1]
        for i in reversed(range(len(num))):
            ans = ans + (ord(num[i])-ord("0"))*10**i
        return ans
    def multiply(self, num1, num2):
    
        if(self.intVal(num1)<10 or self.intVal(num2)<10):
            return str(self.intVal(num1) *self.intVal(num2))
        else:
            n=len(max(num1,num2))
            a=self.intVal(num1)//(10**(n//2))
            b=self.intVal(num1)%(10**(n//2))
            c=self.intVal(num2)//(10**(n//2))
            d=self.intVal(num2)%(10**(n//2))
            ac=self.intVal(self.multiply(str(a),str(c)))
            bd=self.intVal(self.multiply(str(b),str(d)))
            ad_plus_bc=self.intVal(self.multiply(str(a+b),str(c+d)))-ac-bd
            return str((ac*(10**(2*f(n/2)))) + ((ad_plus_bc)*(10**f(n/2)))+bd).split('.')[0]