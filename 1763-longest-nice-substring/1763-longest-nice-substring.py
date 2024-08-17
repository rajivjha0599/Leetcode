class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        data = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in data:
                prefix = self.longestNiceSubstring(s[:i])
                suffix = self.longestNiceSubstring(s[i+1:])
                return prefix if len(prefix)>=len(suffix) else suffix
        return s
            
                        