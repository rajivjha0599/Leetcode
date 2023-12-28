class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<10 and x>=0):
            return True
        rev=0
        temp=x
        c=0
        while(temp>0):
            rev=(rev*(10))+temp%10
            temp=temp//10

        if(rev==x):
            return True
        else:
            return False