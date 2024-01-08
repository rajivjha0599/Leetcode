class Solution:
    @staticmethod
    def rec(input,left,right):
        if(left>=right):
            return input
        else:
            temp=input[left]
            input[left]=input[right]
            input[right]=temp
            return Solution.rec(input,left+1,right-1)
    def reverseString(self, s: List[str]) -> None:
        s=Solution.rec(s,0,len(s)-1)
        