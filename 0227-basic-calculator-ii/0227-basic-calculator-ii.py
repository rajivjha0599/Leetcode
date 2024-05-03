class Solution:
    def calculate(self, s: str) -> int:
        i,cur,prev,res =0,0,0,0
        cur_op ="+"
        while i <len(s):
            c = s[i]
            if c.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur =cur *10 + int(s[i])
                    i+=1
                i-=1
                if cur_op == "+":
                    res += cur
                    prev  = cur
                elif cur_op == "-":
                    res -= cur
                    prev = - cur
                elif cur_op == "*":
                    res -=prev
                    res += prev*cur
                    prev = cur*prev
                else:
                    res -=prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif c != " ":
                cur_op = c
            i+=1
        return res