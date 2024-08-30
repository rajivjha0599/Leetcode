class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        j = 0
        for i in range(len(s)):
            if s[i] == " ":
                ans += s[j:i][::-1] + " "  
                j = i + 1  
        ans += s[j:][::-1]  
        return ans