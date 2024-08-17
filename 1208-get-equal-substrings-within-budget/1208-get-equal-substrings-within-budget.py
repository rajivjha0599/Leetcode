class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currCost =0
        i = 0
        ans=0
        for j in range(len(s)):
            currCost += abs(ord(s[j]) - ord(t[j]))
            while currCost>maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i+=1
            ans=max(ans,j-i+1)
        return ans   
        