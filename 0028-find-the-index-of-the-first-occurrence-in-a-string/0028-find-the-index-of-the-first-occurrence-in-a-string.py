class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nL =  len(needle)
        j =  len(haystack)-1
        i = 0
        while i<=j-nL+1:
            if (len(haystack[i:])<len(needle)):
                return -1
            if(haystack[i:i+nL] == needle):
                return i
        
            i+=1
        return -1