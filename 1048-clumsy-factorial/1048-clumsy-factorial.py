class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        operations = ["*","//","+","-"]
        idx = 0
        for i in range(n-1,0,-1):
            if idx%4 == 0:
                stack[-1] = stack[-1] * i 
            elif idx%4 == 1:
                stack[-1] = int(stack[-1] /i)
            elif idx%4 == 2:
                stack.append(i)
            else:
                stack.append(-i)
            idx+=1
        return sum(stack)