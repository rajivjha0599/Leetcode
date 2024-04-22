class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        ans=0
        for ch in operations:
            if ch.isdigit() or (ch.startswith('-') and ch[1:].isdigit()):
                stack.append(ch)
            elif ch == "C":
                stack.pop()
            elif ch =="D":
                stack.append(int(stack[-1])*2)
            elif ch == "+":
                stack.append(int(stack[-1])+(int(stack[-2])))
        for data in stack:
            ans = ans + int(data)
        return ans