class Solution:
    def firstUniqChar(self, s: str) -> int:
        HM = {}
        for i in range(len(s)):
            if s[i] not in HM:
                HM[s[i]] = 0
            HM[s[i]] += 1
        ans  = ""
        for key,val in HM.items():
            if(val == 1):
                ans = key
                break
        for i in range(len(s)):
            if s[i] == ans:return i
        return -1