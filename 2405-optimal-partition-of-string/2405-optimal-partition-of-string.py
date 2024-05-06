class Solution:
    def partitionString(self, s: str) -> int:
        hash=set()
        res = 1
        for ch in s:
            if ch in hash:
                hash.clear()
                res = res+1
            hash.add(ch)
        return res