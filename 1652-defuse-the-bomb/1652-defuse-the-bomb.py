class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = n*[0] 
        if k ==0:
            return ans
        start = 1 if k>0 else n+k
        end = k if k>0 else n-1
        
        sum = 0
        for i in range(start,end+1):
            sum += code[i]
        
        for i in range(n):
            ans[i] = sum
            sum -= code[start%n]
            start +=1
            end +=1
            sum += code[end%n]
        return ans
            