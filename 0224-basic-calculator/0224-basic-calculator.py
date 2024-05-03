class Solution:
    def calculate(self, s: str) -> int:
        curr,sign,output,stack=0,1,0,[]
        for c in s:
            if c.isdigit():
                curr = (curr*10)+int(c)
            elif c in "+-":
                output+=(curr)*sign
                if c == "+":
                    sign = 1
                else:
                    sign =-1
                curr = 0
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output=0
                sign=1
            elif c == ")":
                output += curr*sign
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output + curr*sign
                