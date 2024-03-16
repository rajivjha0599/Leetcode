class Solution:
    def decodeString(self, s: str) -> str:
        characters=[]
        for i in range(len(s)):
            if(s[i]!="]"):
                characters.append(s[i])
            else:
                substr=""
                while(characters[-1]!="["):
                    substr=characters.pop() + substr
                characters.pop()
                k=""
                while characters and characters[-1].isdigit():   
                    k=characters.pop() + k
                characters.append(int(k)*substr)
        return "".join(characters)
                
            
                