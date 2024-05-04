class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for ch in s:
            if ch =="#":
                if not stack1:
                    continue
                else:
                    stack1.pop()
            else:
                stack1.append(ch)
        for ch in t:
            if ch =="#":
                if not stack2:
                    continue
                else:
                    stack2.pop()
            else:
                stack2.append(ch)
        str1= "".join(stack1)
        str2= "".join(stack2)
        if str1 == str2:return True
        else:return False