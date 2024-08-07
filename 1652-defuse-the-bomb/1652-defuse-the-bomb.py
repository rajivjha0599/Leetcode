class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if(k==0):
                return [0]*len(code)
        temparr = list(code)
        if(k>0):
            
            for i in range(len(code)):
                temp = k
                code[i] = 0
                while temp > 0:
                    code[i] += temparr[(i+temp)%len(temparr)]
                    temp-=1
            return code
        if(k<0):

            for i in range(len(code)):
                temp = k
                code[i] = 0
                while temp < 0:
                    code[i] += temparr[(i+temp)%len(code)]
                    temp+=1
            return code