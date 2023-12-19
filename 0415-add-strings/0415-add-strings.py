class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        result=[]
        while i>-1 or j>-1:
                    d1=ord(num1[i])-ord("0") if i>-1 else 0
                    d2=ord(num2[j])-ord("0") if j>-1 else 0

                    digit=(d1+d2+carry)%10
                    result.append(str(digit))
                    carry=(d1+d2+carry)//10
                    i=i-1
                    j=j-1
        if carry != 0:
                    result.append("1")
        output=(''.join(list(reversed(result))))
        return (output)
            
            