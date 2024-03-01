class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        elif(n==1 or n==3):
            return True
        elif(n%3!=0):
            return False
        else:
            return self.isPowerOfThree(n//3)
            