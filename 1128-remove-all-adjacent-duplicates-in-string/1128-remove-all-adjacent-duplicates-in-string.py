class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            while stack != [] and len(stack)>=2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
        return "".join(stack) if stack else ""
