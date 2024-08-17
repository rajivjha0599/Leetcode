class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""
        def is_nice(s:str):
            data = set(s)
            for c in data:
                if c.islower():
                    if c.upper() not in data:
                        return False
                else:
                    if c.lower() not in data:
                        return False
            return True
        for i in range(len(s)):
            n = len(s)
            for j in range(i+1,n+1):
                subs = s[i:j]
                
                if is_nice(subs) and len(subs)>len(longest):
                    longest = subs
        return longest
                        