class Solution:
    def firstUniqChar(self, s: str) -> int:
        HM = {}
        for i in range(len(s)):
            if s[i] not in HM:
                HM[s[i]] = 0
            HM[s[i]] += 1
        for i,c in enumerate(s):
            if HM[c] == 1:return i
        return -1