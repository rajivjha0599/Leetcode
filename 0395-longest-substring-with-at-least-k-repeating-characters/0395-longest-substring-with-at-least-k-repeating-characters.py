from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        if k <= 1:
            return n
        
        count = Counter(s)
        
        l = 0
        while l < n and count[s[l]] >= k:
            l += 1
        if l >= n:
            return n
        
        ls1 = self.longestSubstring(s[0:l], k)
        while l < n and count[s[l]] < k:
            l += 1
        ls2 = self.longestSubstring(s[l:], k) if l < n else 0
        
        return max(ls1, ls2)
