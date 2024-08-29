class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag=0
        for j in range(len(word)):
            if(word[j] == ch):
                flag = 1
                break
            
        if(j==len(word)-1 and flag !=1):
            return word
        return word[:j+1][::-1]+word[j+1:]
            
        
        