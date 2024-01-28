class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def bT(open,closed):
            if (open==closed==n):
                res.append("".join(stack))
                return
            if(open<n):
                stack.append("(")
                bT(open+1,closed)
                stack.pop()
            if(closed<open):
                stack.append(")")
                bT(open,closed+1)
                stack.pop()
        bT(0,0)
        return res