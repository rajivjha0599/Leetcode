class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        data = defaultdict(int)
        
        for r in range(len(s)):
            data[s[r]] += 1
            while data[s[r]] > 2:
                data[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans