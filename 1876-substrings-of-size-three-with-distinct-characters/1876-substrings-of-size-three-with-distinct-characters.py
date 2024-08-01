class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n - 2):
            a, b, c = s[i], s[i + 1], s[i + 2]
            if a != b and a != c and b != c:
                res += 1
        return res
