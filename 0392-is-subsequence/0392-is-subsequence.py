class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        ans = 0
        while i<len(s):
            while j<len(t):
                if(s[i] == t[j]):
                    ans+=1
                    j+=1
                    break
                j+=1
            if(j==len(t)):
                break
            i+=1
        return True if ans ==  len(s) else False