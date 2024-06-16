class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        lastOcc = {}
        j=-1
        for i,c in enumerate(s):
            j = max(j,lastOcc.get(c,-1))
            ans = max(ans,i-j)
            lastOcc[c] = i  
        return ans