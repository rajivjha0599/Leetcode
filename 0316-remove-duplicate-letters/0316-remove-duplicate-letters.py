class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []  

        for index, ch in enumerate(s):
            if ch in stack:  
                continue
            else:
                while stack and ch < stack[-1] and stack[-1] in s[index + 1:]:
                    stack.pop()
                stack.append(ch)

        return "".join(stack)
